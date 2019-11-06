from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    portfolio_site = models.URLField(blank=True)

def __str__(self):
  return self.user.username

'''class User_Info(AbstractUser):
    username = models.CharField(max_length=150)
    email = models.EmailField()
    password = models.CharField(max_length=20)'''
