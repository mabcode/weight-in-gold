from django.shortcuts import render
from django.http import HttpResponse

import time

def index(request):
    now = time.strftime('%c')
    return HttpResponse("Hello world, it is %s" % now)