# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import generic
from . import models

class Blog(generic.ListView):
    template_name = "blog/home.html"
