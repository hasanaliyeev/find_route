from django.urls import path

from routes import views

urlpatterns = [
    path('', views.home, name='home')
]
