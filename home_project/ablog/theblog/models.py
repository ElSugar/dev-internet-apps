from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date

class Category(models.Model):
  name = models.CharField(max_length=255)

  def __str__(self):
    return str(self.name)
  
  def get_absolute_url(self):
    return reverse('article-detail', args=(str(self.pk)))
    #return reverse('home')

class Post(models.Model):
  title = models.CharField(max_length=255)
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  body = models.TextField()
  date = models.DateTimeField(auto_now_add=True)
  category = models.CharField(max_length=255, default='lifestyle')

  def __str__(self):
    return str(self.title) + ' | ' + str(self.author)
  
  def get_absolute_url(self):
    return reverse('article-detail', args=(str(self.pk)))