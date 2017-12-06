# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse,JsonResponse
from django.views import generic
from django.urls import reverse

from .models import Unit
import json 

def computeWeight(from_unit,to_unit,amount):
	target_unit = Unit.objects.get(name=to_unit)
	source_unit = Unit.objects.get(name=from_unit)
	return target_unit.basis_factor * source_unit.basis_factor * amount


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
			val = computeWeight('pound','tory_ounce',n)
			resp = { 'n': n, 'computeWeight': val }

	return JsonResponse(resp)

def index(request):
    return render(request, 'weightInGold/home.html', {})
    
    