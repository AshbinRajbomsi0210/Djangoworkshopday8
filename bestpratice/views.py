from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

def index(request):
    return render(request, 'bestpratice/home.html')
# Create your views here.
