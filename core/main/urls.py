from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('fruits/', FruitListView.as_view(), name='fruit'),
    path('fruits/<str:slug>/', FruitDetailView.as_view(), name='fruit_detail'),
    path('cars/', CarListView.as_view(), name='car'),
    path('cars/<str:slug>', CarDetailView.as_view(), name='car_detail'),


]