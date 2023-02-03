from django.db import models

class LoginUser(models.Model):
    UserName=models.CharField(max_length=100,unique=True)
    Password=models.CharField(max_length=100,unique=False)
    profile=models.ImageField(upload_to='profilesAdmin/',unique=False)
    def __str__(self):
        return self.UserName

class LoginAdmin(models.Model):
    AdminName=models.CharField(max_length=100,unique=True)
    Password=models.CharField(max_length=100,unique=False)
    profile=models.ImageField(upload_to='profilesAdmin/',unique=False)

    def __str__(self):
        return self.AdminName

