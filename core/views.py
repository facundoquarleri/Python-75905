from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render (request, 'core/index.html')

def aboutme(request):
    return render(request, 'core/aboutme.html')


