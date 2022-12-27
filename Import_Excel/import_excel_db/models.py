from django.db import models

# Create your models here.
class temperature(models.Model):

    year= models.FloatField(max_length=50)
    jan= models.FloatField(max_length=50)
    feb= models.FloatField(max_length=50)
    mar= models.FloatField(max_length=50)
    apr= models.FloatField(max_length=50)
    may= models.FloatField(max_length=50)
    jun= models.FloatField(max_length=50)
    jul= models.FloatField(max_length=50)
    aug= models.FloatField(max_length=50)
    sep= models.FloatField(max_length=50)
    oct= models.FloatField(max_length=50)
    nov= models.FloatField(max_length=50)
    dec= models.FloatField(max_length=50)
    win= models.FloatField(max_length=50)
    spr= models.FloatField(max_length=50)
    sum= models.FloatField(max_length=50)
    aut= models.FloatField(max_length=50)
    ann= models.FloatField(max_length=50)
    def __str__(self):
        return self.year
                 
    objects = models.Manager()
