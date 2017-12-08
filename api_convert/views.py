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

	if not request.GET.has_key('value'):
		resp['error'] = "Usage: value=[non-negative integer]"
	else:
		value = int(request.GET['value'])
		from_unit = request.GET.get('from')
		to_unit = request.GET.get('to')
		
		if (value < 0):
			resp['error'] = "Usage: value=[non-negative integer]"
		else:
			val = computeWeight(from_unit,to_unit,value)
			resp = { 'value': val, 'units': value }

	return JsonResponse(resp)

