from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Restaurant,Review,Comment,Category


def index(request,catid=0):
    context = {}
    category = Category.objects.all()

    cat_dict = dict()
    print(category.get(Cid=1))


    for dd in category:
        print(dd.Cid)
        cat_dict[dd.Cid] = dd.Cname

    weather = Restaurant.objects.all()
    context = {
        'cat': cat_dict,
        'restaurant': weather,
    }



    return render(request, 'home.html', context)

