from ast import keyword
import turtle
from django.db import models
from django.db.models import Avg, Count
from django.core.validators import MaxValueValidator, MinValueValidator

class Rating(models.Model):
    r_bname= models.CharField(max_length=50, blank=True)
    r_sname= models.CharField(max_length=20)
    r_fname= models.CharField(max_length=20)
    r_message = models.TextField(max_length=200, blank=True)
    rating= models.IntegerField(default=1)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.r_sname + " " + self.r_fname)


class Contact(models.Model):
    c_bname= models.CharField(max_length=50, blank=True)
    c_sname= models.CharField(max_length=20)
    c_fname= models.CharField(max_length=20)
    c_email= models.CharField(max_length=30)
    c_pnumber =  models.CharField(max_length=20)
    c_message = models.TextField(max_length=200, blank=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.c_sname + " " + self.c_fname)