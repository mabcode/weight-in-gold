# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone 

class Article(models.Model):
    title = models.CharField(max_length=200)
    authors_name = models.CharField(max_length=200)
    content = models.TextField()
    published = models.BooleanField(default=True)
    posted_date  = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
        
class Comments(models.Model):
    blog = models.ForeignKey(Article, on_delete=models.CASCADE)
    commenters_nickname = models.CharField(max_length=200)
    email_address = models.EmailField()
    content = models.TextField()
    posted_date  = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
  