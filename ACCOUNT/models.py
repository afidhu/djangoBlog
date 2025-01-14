from django.db import models

from django.contrib.auth.models import AbstractUser
# Create your models here.

class Users(AbstractUser):
    controller=models.BooleanField(default=False)
    poster=models.BooleanField(default=False)
    is_status=models.BooleanField(default=True)
    approve=models.BooleanField(default=False)
    
    def __str__(self):
        return self.username
    
    

class Profile(models.Model):
    author=models.OneToOneField(Users, on_delete=models.CASCADE)
    image=models.ImageField(default='user.png',upload_to='profile/')
    
    def __str__(self) -> str:
        return self.author.username
   