# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic
from django.urls import reverse

from .models import Home


class HomeView(generic.ListView):
    template_name = 'weightInGold/home.html'
    context_object_name = 'input'
    def get_queryset(self):
        Home.objects.order_by('-posted_date')