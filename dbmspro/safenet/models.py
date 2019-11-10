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

class User_Info(models.Model):
	usid = models.CharField(max_length=5, primary_key=True)
	name = models.CharField(max_length=30)
	email = models.CharField(max_length=50)
	password = models.CharField(max_length=100)

class Bookings(models.Model):
	urlid = models.CharField(max_length=5, primary_key=True)
	name = models.CharField(max_length=50)
	url = models.CharField(max_length=100)

class ECommerce(models.Model):
	urlid = models.CharField(max_length=5, primary_key=True)
	name = models.CharField(max_length=50)
	url = models.CharField(max_length=100)

class Entertainment(models.Model):
	urlid = models.CharField(max_length=5, primary_key=True)
	name = models.CharField(max_length=50)
	url = models.CharField(max_length=100)

class Games(models.Model):
	urlid = models.CharField(max_length=5, primary_key=True)
	name = models.CharField(max_length=50)
	url = models.CharField(max_length=100)

class Illegal(models.Model):
	urlid = models.CharField(max_length=5, primary_key=True)
	name = models.CharField(max_length=50)
	url = models.CharField(max_length=100)

class Messaging(models.Model):
	urlid = models.CharField(max_length=5, primary_key=True)
	name = models.CharField(max_length=50)
	url = models.CharField(max_length=100)

class News(models.Model):
	urlid = models.CharField(max_length=5, primary_key=True)
	name = models.CharField(max_length=50)
	url = models.CharField(max_length=100)

class SocialMedia(models.Model):
	urlid = models.CharField(max_length=5, primary_key=True)
	name = models.CharField(max_length=50)
	url = models.CharField(max_length=100)

class Plan(models.Model):
	usid = models.OneToOneField(User_Info, on_delete=models.CASCADE, primary_key=True)
	bookings = models.CharField(max_length=100)
	ecommerce = models.CharField(max_length=100)
	entertainment = models.CharField(max_length=100)
	games = models.CharField(max_length=100)
	illegal = models.CharField(max_length=100)
	messaging = models.CharField(max_length=100)
	news = models.CharField(max_length=100)
	socialMedia = models.CharField(max_length=100)

class Custom(models.Model):
	usid = models.OneToOneField(User_Info, on_delete=models.CASCADE)
	block = models.CharField(max_length=100)
	redirect = models.CharField(max_length=100)

	class Meta:
		unique_together = [['usid', 'block']]