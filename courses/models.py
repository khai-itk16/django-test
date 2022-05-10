from enum import unique
from unicodedata import category
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    avartar = models.ImageField(upload_to='uploads/%Y/%m')


class Category(models.Model):
    name = models.CharField(max_length=100, null=False, unique=True)

    def __str__(self):
        return self.name


class ItemBase(models.Model):
    class Meta:
        abstract = True

    subject = models.CharField(max_length=100, null=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)


class Course(ItemBase):
    class Meta:
        unique_together = ('subject', 'category')

    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.subject


class Lesson(ItemBase):
    class Meta:
        unique_together = ('subject', 'course')

    content = models.TextField()
    image = models.ImageField(upload_to='lessons/%Y/%m')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag', blank=True, null=True)

    def __str__(self):
        return self.subject


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


