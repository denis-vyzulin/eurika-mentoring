from django.db import models
from os.path import getsize

from django_extensions.db.models import TimeStampedModel
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, BaseUserManager, AbstractBaseUser

from django.utils import timezone
from django.core.mail import send_mail
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def _create_user(
        self, email, username, surname, patronymic, password=None,
        **extra_fields):
        '''
        Creates and saves a User with the given email, name, surname,
        patronymic and password.
        '''
        if not email:
            raise ValueError(_('Users must have an email address.'))
        if not username:
            raise ValueError(_('Users must have a username.'))
        if not surname:
            raise ValueError(_('Users must have a surname.'))

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            surname=surname,
            patronymic=patronymic,
            **extra_fields,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(
        self, email, username, surname, patronymic, password=None,
        **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, username, surname, patronymic, password, **extra_fields)

    def create_superuser(
        self, email, username, surname, patronymic, password=None,
        **extra_fields):
        '''
        Creates and saves a superuser with the given email, username, surname,
        patronymic and password.
        '''
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, username, surname, patronymic, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        _('Email address'),
        max_length=255,
        unique=True,
        help_text=_(
            'Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'
        ),
        validators=[], #! Need validate
        error_messages={
            'unique': _('A user with that email already exists.')
        }
    )
    # password field supplied by AbstractBaseUser

    username = models.CharField(_('Name'), max_length=30)
    surname = models.CharField(_('Surname'), max_length=30)
    patronymic = models.CharField(_('Patronymic'), max_length=30)
    
    # last_login field supplied by AbstractBaseUser
    is_active = models.BooleanField(
        _('Active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active.'
            'Unselect this instead of deleting accounts.'
        )
    )
    is_staff = models.BooleanField(
        _('Staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.'
        )
    )
    date_joined = models.DateTimeField(_("Date joined"), default=timezone.now)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'surname', 'patronymic']

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
        
    def get_full_name(self):
        '''
        Return username, surname and patronymic with a spaces in between.
        '''
        full_name = '%s %s %s' % (self.username, self.surname, self.patronymic)
        return full_name.strip()
    
    def get_short_name(self):
        '''
        Return the short name for the user.
        '''
        return self.username
    
    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Send an email to this user.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def __str__(self):
        return self.get_full_name()


class University(models.Model):
    name = models.CharField(_('Name of university'), max_length=128, db_index=True)

    class Meta:
        verbose_name = _('University')
        verbose_name_plural = _('Universities')

    def __str__(self):
        return self.name


class Mentor(User):
    university_id = models.ForeignKey(University, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = _('Mentor')
        verbose_name_plural = _('Mentors')

    def __str__(self):
        return self.get_full_name()


class School(models.Model):
    name = models.CharField(_('Name of school'), max_length=128)

    class Meta:
        verbose_name = _('School')
        verbose_name_plural = _('Schools')

    def __str__(self):
        return self.name


class Student(User):
    SCHOOL_NUM = (
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
    )

    school_id = models.ForeignKey(School, on_delete=models.SET_NULL, null=True)
    school_num = models.CharField(_('School number'), choices=SCHOOL_NUM, default='8', max_length=2)

    class Meta:
        verbose_name = _('student')
        verbose_name_plural = _('students')

    def __str__(self):
        return self.get_full_name()


class Publication(TimeStampedModel):
    cover = models.ImageField(_('Upload image'), upload_to='publications/covers/')
    title = models.CharField(_('Title'), max_length=125)
    text = models.TextField(_('Description'))

    class Meta:
        verbose_name = _('Publication')
        verbose_name_plural = _('Publications')

    def __str__(self):
        return self.title


class PublicationImage(TimeStampedModel):
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE, verbose_name=_('Publication id'))
    image = models.ImageField(_('Upload image'), upload_to='publications/images/',
                            null=True, blank=True)

    class Meta:
        verbose_name = _('Image')
        verbose_name_plural = _('Images')

    def __str__(self):
        return self.image.name


class Document(TimeStampedModel):
    file = models.FileField(_('Upload file'), upload_to='documents/')
    name = models.CharField(_('Filename'), max_length=125)

    class Meta:
        verbose_name = _('Document')
        verbose_name_plural = _('Documents')

    def __str__(self):
        return self.name

    @property
    def filesize(self):
        return getsize(self.file)


class Direction(TimeStampedModel):
    name = models.CharField(_('Direction name'), max_length=125)

    class Meta:
        verbose_name = _('Direction')
        verbose_name_plural = _('Directions')

    def __str__(self):
        return self.name


class Project(TimeStampedModel):
    title = models.CharField(_('Title'), max_length=125)
    direction = models.ForeignKey(Direction, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(_('Description'))

    class Meta:
        verbose_name = _('Project')
        verbose_name_plural = _('Projects')

    def __str__(self):
        return self.title


class ProjectFile(TimeStampedModel):
    file = models.FileField(_('Upload file'), upload_to='projects/{{ request.user.name }}/documents/')
    filename = models.CharField(_('Filename'), max_length=255, null=True, blank=True,
                        help_text=_('This field change the filename displayed on the site'))
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name=_('Project id'))

    class Meta:
        verbose_name = _('File')
        verbose_name_plural = _('Files')

    def __str__(self):
        return self.file.name

    @classmethod
    def name(self):
        return self.file.name.split('/')[-1]

    
class ProjectStudent(TimeStampedModel):
    student = models.ForeignKey(Student, on_delete=models.PROTECT, verbose_name=_('Student id'))
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name=_('Project id'))

    class Meta:
        verbose_name = _('Student')
        verbose_name_plural = _('Students')

    def __str__(self):
        return self.student