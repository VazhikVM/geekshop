from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime, timedelta
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
import pytz


class ShopUser(AbstractUser):
    avatar = models.ImageField(upload_to='user_avatar', blank=True, verbose_name='Аватар')
    age = models.PositiveSmallIntegerField(verbose_name='Возраст', blank=True, null=True)

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


class ShopUserProfile(models.Model):

    MALE = 'М'
    FEMALE = 'Ж'
    OTHERS = 'О'

    GENDER = (
        (MALE, 'Мужской'),
        (FEMALE, 'Женский'),
        (OTHERS, 'Иное'),
    )

    user = models.OneToOneField(ShopUser, null=False, unique=True, on_delete=models.CASCADE, db_index=True)
    tagline = models.CharField(max_length=128, verbose_name='Тэги', blank=True)
    about_me = models.TextField(verbose_name='Обо мне')
    gender = models.CharField(max_length=20, choices=GENDER, default=OTHERS, verbose_name='Пол')

    @receiver(post_save, sender=ShopUser)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            ShopUserProfile.objects.create(user=instance)

    @receiver(post_save, sender=ShopUser)
    def update_user_profile(sender, instance, **kwargs):
        instance.shopuserprofile.save()
