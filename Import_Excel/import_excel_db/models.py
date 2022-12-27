from django.db import models

# Create your models here.
class temperature(models.Model):

    year= models.CharField(max_length=50)
    jan= models.CharField(max_length=50)
    feb= models.CharField(max_length=50)
    mar= models.CharField(max_length=50)
    apr= models.CharField(max_length=50)
    may= models.CharField(max_length=50)
    jun= models.CharField(max_length=50)
    jul= models.CharField(max_length=50)
    aug= models.CharField(max_length=50)
    sep= models.CharField(max_length=50)
    oct= models.CharField(max_length=50)
    nov= models.CharField(max_length=50)
    dec= models.CharField(max_length=50)
    win= models.CharField(max_length=50)
    spr= models.CharField(max_length=50)
    sum= models.CharField(max_length=50)
    aut= models.CharField(max_length=50)
    ann= models.CharField(max_length=50)
    def __str__(self):
        return self.year
                 
    objects = models.Manager()
