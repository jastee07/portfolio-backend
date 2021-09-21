from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
