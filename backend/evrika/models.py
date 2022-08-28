from django.db import models

from django.contrib.auth.models import PermissionsMixin, BaseUserManager, AbstractBaseUser
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.core.mail import send_mail


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
        _('email address'),
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

    username = models.CharField(_('name'), max_length=30)
    surname = models.CharField(_('surname'), max_length=30)
    patronymic = models.CharField(_('patronymic'), max_length=30)
    
    # last_login field supplied by AbstractBaseUser
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active.'
            'Unselect this instead of deleting accounts.'
        )
    )
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.'
        )
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'surname', 'patronymic']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        
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
    name = models.CharField(_('name of unversity'), max_length=128, db_index=True)

    class Meta:
        verbose_name = _('university')
        verbose_name_plural = _('universities')

    def __str__(self):
        return self.name


class Mentor(User):
    university_id = models.ForeignKey(University, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = _('mentor')
        verbose_name_plural = _('mentors')

    def __str__(self):
        return self.get_full_name()


class School(models.Model):
    name = models.CharField(_('name of school'), max_length=128)

    class Meta:
        verbose_name = _('school')
        verbose_name_plural = _('schools')

    def __str__(self):
        return self.name


class Student(User):
    school_id = models.ForeignKey(School, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = _('student')
        verbose_name_plural = _('students')

    def __str__(self):
        return self.get_full_name()