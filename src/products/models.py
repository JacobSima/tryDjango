from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
  title = models.CharField(max_length=120) # max_length = required
  description = models.TextField(blank=True,null=True)
  price = models.DecimalField(decimal_places=2,max_digits=10000)
  summary = models.TextField(blank=False,null=False)  # not required with blank=True and the old Product may stay without it with null =true
  # blank is to do with how the field is render, as required or not
  # null is to do with the database, if True then old item in database can remains without it
  # if False then each it has to be added in old item with default value. 
  featured = models.BooleanField(default=False)  

  def __str__(self):
    return self.title

  def get_absolute_url(self):
    # return f"/products/{self.id}/"
    return reverse('products:dynamic_lookup',kwargs={'my_id':self.id})
    

