from django.db import models

from django.urls import reverse
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):

    def get_absolute_url(self):
        return reverse('users:users_detail', args=[self.pk])

    @property
    def get_uid(self):
        return self.uid

    @get_uid.setter
    def get_uid(self, value):
        if not self.uid:
            self.uid = value
