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
        self, email, username, surname, patronymic=None, password=None,
        **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, username, surname, patronymic, password, **extra_fields)

    def create_superuser(
        self, email, username, surname, patronymic=None, password=None,
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
    patronymic = models.CharField(_('Patronymic'), max_length=30, null=True, blank=True)

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
    REQUIRED_FIELDS = ['username', 'surname']

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
    name = models.CharField(_('Name of university'), max_length=128,
                            db_index=True)

    class Meta:
        verbose_name = _('University')
        verbose_name_plural = _('Universities')

    def __str__(self):
        return self.name


class Mentor(User):
    university_id = models.ForeignKey(University, on_delete=models.SET_NULL,
                                      null=True, verbose_name=_('Unversity'))

    class Meta:
        verbose_name = _('Mentor')
        verbose_name_plural = _('Mentors')

    def __str__(self):
        return self.get_full_name()


class School(models.Model):
    name = models.CharField(_('School name'), max_length=128)

    class Meta:
        verbose_name = _('School')
        verbose_name_plural = _('Schools')

    def __str__(self):
        return self.name


class Student(User):
    CLASS_NUM = (
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
    )

    school_id = models.ForeignKey(School, on_delete=models.SET_NULL,
                                  null=True, verbose_name=_('School'))
    class_num = models.CharField(_('Class number'), choices=CLASS_NUM,
                                 default='7', max_length=2)

    class Meta:
        verbose_name = _('Student')
        verbose_name_plural = _('Students')

    def __str__(self):
        return self.get_full_name()


class Article(TimeStampedModel):
    ARTICLE_TYPES = (
        ('News', 'Новости'),
        ('Study', 'Обучение'),
        ('Results', 'Результаты'),
    )

    type = models.CharField(_('Choose type'), choices=ARTICLE_TYPES, default='News', max_length=40)
    cover = models.ImageField(_('Upload image'), upload_to='articles/covers/')
    title = models.CharField(_('Title'), max_length=125)
    text = models.TextField(_('Description'))

    class Meta:
        verbose_name = _('Article')
        verbose_name_plural = _('Articles')

    def __str__(self):
        return self.title


class Subject(TimeStampedModel):
    name = models.CharField(_('Subject name'), max_length=125)

    class Meta:
        verbose_name = _('Subject')
        verbose_name_plural = _('Subjects')

    def __str__(self):
        return self.name


class Project(TimeStampedModel):
    title = models.CharField(_('Title'), max_length=125)
    description = models.TextField(_('Description'))
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True,
                                blank=True, verbose_name=_('Subject'))
    is_display = models.BooleanField(_('Display on the site'))
    is_complete = models.BooleanField(_('Complete status'))
    users_view = models.PositiveIntegerField(_('Project views'), editable=False)
    author = models.ForeignKey(Mentor, on_delete=models.SET_NULL, null=True,
                               blank=True, verbose_name=_('Author'))
    implementer = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True,
                                    blank=True, verbose_name=_('Implementer'))

    class Meta:
        verbose_name = _('Project')
        verbose_name_plural = _('Projects')

    def __str__(self):
        return self.title


class Response(TimeStampedModel):
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE, null=False,
                                   blank=False, verbose_name=_('Project'))
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE, null=False,
                                   blank=False, verbose_name=_('Student'))
    message = models.TextField(_('Message'))

    class Meta:
        verbose_name = _('Response')
        verbose_name_plural = _('Responses')

    def __str__(self):
        return self.student_id.get_full_name


class ProjectFile(TimeStampedModel):
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE, null=False,blank=False, verbose_name=_('Project'))
    file = models.FileField(_('Upload file'), upload_to='projects/{{request.user.name}}/documents/')
    filename = models.CharField(_('Filename'), max_length=255, null=True, blank=True,
                        help_text=_('This field change the filename displayed on the site'))

    class Meta:
        verbose_name = _('Project File')
        verbose_name_plural = _('Project Files')

    def __str__(self):
        return self.file.name

    @classmethod
    def name(self):
        return self.file.name.split('/')[-1]


class Announcement(TimeStampedModel):
    ANNOUNCEMENT_TYPES = (
        ('Online', 'Онлайн'),
        ('Offline', 'Оффлайн'),
    )

    type = models.CharField(_('Announcement\'s type'), choices=ANNOUNCEMENT_TYPES, default='Online', max_length=80)
    text = models.TextField(_('Description'))
    venue = models.CharField(_('Venue'), max_length=510)
    date_venue = models.DateTimeField(_('Date of venue'))
