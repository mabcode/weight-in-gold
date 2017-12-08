# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Unit(models.Model):
    name = models.CharField(max_length=200)
    basis_factor = models.FloatField(default=0)
    
    def __str__(self):
        return self.name 