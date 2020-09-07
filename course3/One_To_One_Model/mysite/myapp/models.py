from django.db import models
## this is the django Validator validator
## use to validate model in the model field
from django.core.validators import MinLengthValidator

class Breed(models.Model):
    ## this is the Breed of the Cat
    ## max length can be added with the max_length
    ## we add the min length with the validator
    name = models.CharField(max_length=200,validators=[MinLengthValidator(2,'Breed must be greater than 1 character')])

    def __str__(self):
        return self.name

class Cat(models.Model):
    nickname = models.CharField(max_length=200,validators=[MinLengthValidator(2,'Nickname must be greater than 1 character')])
    weight   = models.PositiveIntegerField()
    foods    = models.CharField(max_length=300)
    breed    = models.ForeignKey(Breed,on_delete=models.CASCADE,null=False)

    def __str__(self):
        return self.nickname 