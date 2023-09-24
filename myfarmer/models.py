from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class customuser(AbstractUser):
    user = ( 
        (1,'Admin'),
        (2,'expert'),
        (3,'farmer'),
      )
    
    user_type = models.CharField(choices=user,max_length=58,default=1)
    
class Farmer(models.Model):
  admin = models.OneToOneField(customuser,on_delete=models.CASCADE)
  name = models.CharField(max_length=50)
  
  def __str__(self):
    return self.admin.username  


