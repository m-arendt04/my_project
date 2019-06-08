from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Topics(models.Model):
    title = models.CharField(max_length=256, verbose_name='Tytuł')
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=True, default=None)


class Post(models.Model):
    title = models.CharField(max_length=128, verbose_name='Tytuł')
    content = models.TextField(verbose_name='Zawartość')
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=True, default=None)
    topic = models.ForeignKey(Topics, on_delete=models.CASCADE, default=None)

