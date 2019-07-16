from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Restaurant,Review,Comment,Category


def index(request):
    context = {}
    category = Category.objects.all()

    weather = Restaurant.objects.all()
    context = {
        'cat': category,
        'restaurant': weather,
    }



    return render(request, 'home.html', context)

