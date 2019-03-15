from django.db.models.signals import post_init, post_save
from django.dispatch import receiver
from django.db.models.signals import pre_delete
from django.db import models
from django.shortcuts import *
# Create your models here.
import os
from django.conf import settings


class AudioFile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='user_audio/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (self.name)


class Button(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    audio = models.ForeignKey(
        AudioFile,
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=7, default="#00ff00")

    preset_list = (
        ('0', 0), ('1', 1), ('2', 2), ('3', 3)
    )
    preset = models.CharField(
        max_length=1,
        choices=preset_list,
        default='0',
    )

    def __str__(self):
        return (self.name)


class Pad(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    name = models.CharField(max_length=255)
    buttonlist = models.ManyToManyField(Button, blank=True)


@receiver(pre_delete, sender=AudioFile)
def audiofile_delete(sender, instance, **kwargs):
    instance.file.delete(False)
