from django.db import models
from django.shortcuts import reverse

# Create your models here.
class Blog (models.Model):
  title   = models.CharField(max_length=120)
  content = models.TextField()
  active  = models.BooleanField(default=True)

  def get_absolute_url(self):
    return reverse('blogs:detail_view',kwargs={'id':self.id})    # It is part of the CreateView class, this redirect you detail_view by default

 






