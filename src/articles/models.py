from django.db import models
from django.urls import reverse

# Create your models here.
class Article(models.Model):
  title = models.CharField(max_length=200)
  description = models.CharField(max_length=200, blank=True)
  price = models.DecimalField(max_digits=100000, decimal_places=2)
  summary = models.TextField(blank=False, default="It is the summary")
  is_sold = models.BooleanField(default=True)

  def __str__(self):
    return self.title

  def get_absolute_url(self):
    # return "/articles/%i/" % self.id
    
    # passe the main url or app_name:articles, the page name at urls:article_detail
    # then the kwargs for the query as id in this case
    return reverse('articles:article_detail',kwargs={'id':self.id})

