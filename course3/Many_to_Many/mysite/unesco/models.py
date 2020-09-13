from django.db import models

class Category(models.Model):
    name          = models.CharField(max_length=128,null=True,blank=True)
    
    def __str__(self):
        return self.name 

class States(models.Model):
    name          = models.CharField(max_length=128,null=True,blank=True)

    def __str__(self):
        return self.name

class Region(models.Model):
    name          = models.CharField(max_length=128,null=True,blank=True)

    def __str__(self):
        return self.name 

class Iso(models.Model):
    name          = models.CharField(max_length=128,null=True,blank=True)

    def __str__(self):
        return self.name

class Site(models.Model):
    name          = models.CharField(max_length=128)
    description   = models.TextField(null=True,blank=True)
    justification = models.TextField(null=True,blank=True)
    year          = models.IntegerField(null=True)
    longitude     = models.CharField(max_length=128)
    latitude      = models.CharField(max_length=128)
    area_hectares = models.CharField(max_length=128)
    category      = models.ForeignKey(Category,on_delete=models.CASCADE)
    states        = models.ForeignKey(States,on_delete=models.CASCADE)
    region        = models.ForeignKey(Region,on_delete=models.CASCADE)
    iso           = models.ForeignKey(Iso,on_delete=models.CASCADE)


    def __str__(self):
        return self.name
    




