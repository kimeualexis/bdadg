from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    fname = models.CharField(max_length=20)
    sname = models.CharField(max_length=20)
    cover = models.FileField()
    bio = models.CharField(max_length=50)
    area_raised = models.CharField(max_length=50)
    primary_sch = models.CharField(max_length=50)
    high_sch = models.CharField(max_length=50)
    campus = models.CharField(max_length=50, blank=True)
    course = models.CharField(max_length=50, blank=True)
    hobby = models.CharField(max_length=50)
    year_joined_library = models.CharField(max_length=4)
    profession = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.fname

    def get_absolute_url(self):
        return reverse('users:users-index')



