from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Fruit, Car
# Create your views here.



class HomeListView(ListView):
    template_name = 'home.html'

    def get(self, request):
        return render(request, self.template_name)

class FruitListView(ListView):
    template_name = 'fruit.html'

    def get(self, request):
        fruits = Fruit.objects.all()
        return render(request, self.template_name, {'fruits':fruits})


class FruitDetailView(DetailView):
    template_name = 'fruit_detail.html'

    def get(self, request, slug):
        fruit = Fruit.objects.get(slug=slug)
        return render(request, self.template_name, {'fruit':fruit})



class CarListView(ListView):
    template_name = 'car.html'

    def get(self, request):
        cars = Car.objects.all()
        return render(request, self.template_name, {'cars':cars})

class CarDetailView(DetailView):
    template_name = 'car_detail.html'

    def get(self, request, slug):
        car = Car.objects.get(slug=slug)
        return render(request, self.template_name, {'car':car})