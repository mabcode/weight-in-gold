# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone 

class Home(models.Model):
    title = models.CharField(max_length=200)
    posted_date  = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title