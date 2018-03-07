# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.http import JsonResponse

def index(request):
    if request.method == 'POST':
        # POST functionality is a placeholder. Return value is arbitrary
        return HttpResponse('')
    elif request.method == 'GET':
        if 'application/json' in request.META.get('HTTP_ACCEPT'):
            return JsonResponse({"message": "Good morning"})
        else:
            return HttpResponse('<p>Hello, world!</p>')