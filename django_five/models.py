import uuid

from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, )
    slug = models.SlugField(unique=True, default=uuid.uuid1)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=250, unique=True, db_index=True)
    avatar = models.ImageField(null=True, upload_to='profile_images')
    bio = models.TextField()

    def __str__(self):
        return self.user.username


class ContactInfo(models.Model):
    contact = models.CharField(max_length=50, verbose_name='contact', null=True)
    contact_info = models.TextField(max_length=50, verbose_name='contact_info', null=True)

    def __str__(self):
        return self.contact_info

class ReviewModel(models.Model):
    comment = models.TextField(max_length=300)
    date = models.DateField(auto_now=True)


    def __str__(self):
        return self.comment

