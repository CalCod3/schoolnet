from django.db import models

# Create your models here.

class Contact(models.Model):
    first_name = models.CharField(max_length=20, null=True)
    last_name = models.CharField(max_length=20, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    message = models.TextField(max_length=300,blank=True, null=True)

    def __str__(self):
        return self.first_name