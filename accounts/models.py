from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import ImsUserManager


class ImsUser(AbstractBaseUser, PermissionsMixin):
    username = None

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(_("email address"), unique=True)
    phone = models.CharField(verbose_name="Phone Number", max_length=13)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = ImsUserManager()

    def __str__(self):
        return self.email
