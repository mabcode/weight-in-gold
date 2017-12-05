# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic
from django.urls import reverse

from .models import Unit
import json 


#class HomeView(generic.ListView):
#    template_name = 'weightInGold/home.html'
#    context_object_name = 'input'
#    def get_queryset(self):
#        Home.objects.order_by('-posted_date')
        
def computeWeight(n):
	if (n == 0):
		return 0
	elif (n == 1):
		return 1
	else:
		return computeWeight(n-1) + computeWeight(n-2)


def weightAPI(request):
	#for k, v in request.GET.items():   # DELETE ME
	#	print k, "=>", v   # DELETE ME

	resp = {}

	if not request.GET.has_key('n'):
		resp['error'] = "Usage: n=[non-negative integer]"
	else:
		n = int(request.GET['n'])
		if (n < 0):
			resp['error'] = "Usage: n=[non-negative integer]"
		else:
			val = computeWeight(n)
			resp = { 'n': n, 'computeWeight': val }

	return HttpResponse(json.dumps(resp))

def index(request):
    return render(request, 'weightInGold/home.html', {})
    
    