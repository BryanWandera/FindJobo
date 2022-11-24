from django.shortcuts import render
from findjoboapp.models import *

def home_view(request, city="nairobi" ):

    context = {
        "jobs" : Job.objects.filter(city__name=city.lower()) ,
        "selected_city" : city,
        "categories": Category.objects.all(),
        "cities" : City.objects.all()
    }
    return render(request, "index.html", context)




