import datetime

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

dt = datetime.date.today()

def home(request):
    return render(request, 'home.html', {'date': dt})

def about(request):
    return render(request, 'about.html')
