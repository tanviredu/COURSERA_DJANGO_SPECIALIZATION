from django.db import models
from django.core.validators import MaxLengthValidator
from django.contrib.auth.models import User
from django.conf import settings

class Ad(models.Model):
    title      = models.CharField(max_length=200,validators=[MaxLengthValidator(2,"Title must be greater then 2 characters")])
    price      = models.DecimalField(max_digits=7,decimal_places=2,null=True)
    text       = models.TextField()
    owner      = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

        
         
