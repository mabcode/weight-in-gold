# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse,JsonResponse
from django.views import generic
from django.urls import reverse

def index(request):
    return render(request, 'weightInGold/home.html', {})


    
    