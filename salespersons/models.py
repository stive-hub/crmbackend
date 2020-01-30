import datetime
from django.db import models

from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin,
                                        UserManager)
from salespersons.utils import ROLES


class SalesPersonUser(AbstractBaseUser, PermissionsMixin, models.Model):
    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(('date joined'), auto_now_add=True)
    role = models.CharField(max_length=50, choices=ROLES)
    manager = models.ForeignKey(
        'self', null=True, related_name="salesperson", on_delete=models.DO_NOTHING)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', ]

    objects = UserManager()

    def _str_(self):
        return f"<SalesPersonUser : {self.first_name} {self.last_name}>"

    def __repr__(self):
        return self.__str__()

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        full_name = None
        if self.first_name or self.last_name:
            full_name = self.first_name + " " + self.last_name
        elif self.username:
            full_name = self.username
        else:
            full_name = self.email
        return full_name

    def __str__(self):
        return self.email

    class Meta:
        ordering = ['-is_active']

