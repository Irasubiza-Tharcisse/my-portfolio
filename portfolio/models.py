from django.db import models

# Create your models here.
class contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.CharField(max_length=100)
    def __str__(self):
        return f'sent by: {self.name}'
        
class about_me(models.Model):
    description = models.TextField(max_length=1000)
    def __str__(self):
        return f'about me: {self.description}'

class skill(models.Model):
    name = models.CharField(max_length=100)
    languages = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    def __str__(self):
        return f'{self.name}'

class project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    link = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    def __str__(self):
        return f'{self.name}'
    
