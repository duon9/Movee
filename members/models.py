from django.db import models
from django.contrib.auth.hashers import make_password, check_password

# Create your models here.
class Member(models.Model):
    id = models.IntegerField(primary_key= True)
    username = models.CharField(max_length=255, unique= True, null= False)
    password = models.CharField(max_length=255, null = False)
    firstname = models.CharField(max_length=255, null = True)
    lastname = models.CharField(max_length=255, null = True)
    phone = models.CharField(max_length= 20, null = True)
    email = models.CharField(max_length= 255, null= True)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
    
class Movie(models.Model):
    title = models.CharField(max_length= 255, null= False, unique= True)
    description = models.CharField(max_length=255, null = True, unique= False)
    source = models.CharField(max_length=255, null= True)
    image_src = models.CharField(max_length=255, null= True)


