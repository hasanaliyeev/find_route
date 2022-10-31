import datetime

from django.http import HttpResponse
from django.shortcuts import render

dt = datetime.date.today()
def home(request):
    return render(request, 'home.html', {'date':dt})

def about(request):
    return render(request, 'about.html')

def news(request):
    pass
