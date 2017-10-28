# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

import time

def index(request):
    now = time.strftime('%c')
    return HttpResponse("Hello, you are in the polls index. Time is %s" % now)

# Create your views here.
