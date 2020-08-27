from django.db import models

class Publisher(models.Model):
    '''Book Publisher Properties '''
    name    = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city    = models.CharField(max_length=30)
    state   = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    class Meta:
        ordering = ['-name']

    def __str__(self):
        return self.name


class Author(models.Model):
    saluation = models.CharField(max_length=10)  ## Dr. Prof. Mr.Mrs
    name      = models.CharField(max_length=40)
    email     = models.EmailField()
    headshoot = models.ImageField(upload_to="author_headshots")

    def __str__(self):
        return self.name

class Book(models.Model):
    title     = models.CharField(max_length=100)
    authors   = models.ManyToManyField('Author')
    publisher = models.ForeignKey(Publisher,on_delete=models.CASCADE)
    publication_date = models.DateField()


    def __str__(self):
        return self.title 

        

    
    