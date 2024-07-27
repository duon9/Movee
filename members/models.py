from django.db import models

# Create your models here.
class Member(models.Model):
    id = models.IntegerField(primary_key= True)
    username = models.CharField(max_length=255, unique= True, null= False)
    password = models.CharField(max_length=255, null = False)
    firstname = models.CharField(max_length=255, null = True)
    lastname = models.CharField(max_length=255, null = True)
    phone = models.CharField(max_length= 20, null = True)
    email = models.CharField(max_length= 255, null= True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

