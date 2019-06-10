from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    job_title = models.CharField(max_length=50, null=True, blank=True)
    personal_url = models.URLField(max_length=555, blank=True, null=True)
    facebook_account = models.URLField(max_length=255, blank=True, null=True)
    twitter_account = models.URLField(max_length=255, blank=True, null=True)
    github_account = models.URLField(max_length=255, blank=True, null=True)
    linkedin_account = models.URLField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.username
