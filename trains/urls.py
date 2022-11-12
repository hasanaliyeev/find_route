from django.urls import path
from . import views

urlpatterns = [
    path('', views.TrainListView.as_view(), name='home'),
    path('add/', views.TrainCreateView.as_view(), name='create'),
    path('detail/<int:pk>/', views.TrainDetailView.as_view(), name='detail'),
    path('delete/<int:pk>/', views.TrainDeleteView.as_view(), name='delete'),
    path('update/<int:pk>/', views.TrainUpdateView.as_view(), name='update'),
    path('city/<int:pk>/', views.from_city, name='from'),
]
