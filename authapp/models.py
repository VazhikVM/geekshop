from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime, timedelta
from django.conf import settings
import pytz


class ShopUser(AbstractUser):
    avatar = models.ImageField(upload_to='user_avatar', blank=True, verbose_name='Аватар')
    age = models.PositiveSmallIntegerField(verbose_name='Возраст')

    activate_key = models.CharField(max_length=128, verbose_name='Ключ активации', blank=True, null=True)
    activate_key_expired = models.DateTimeField(blank=True, null=True)

    def is_activate_key_expired(self):
        if datetime.now(pytz.timezone(settings.TIME_ZONE)) > self.activate_key_expired + timedelta(hours=48):
            return True
        return False

    def delete(self):
        if self.is_active:
            self.is_active = False
        else:
            self.is_active = True
        self.save()

    def activate_user(self):
        self.is_active = True
        self.activate_key = None
        self.activate_key_expired = None
        self.save()
