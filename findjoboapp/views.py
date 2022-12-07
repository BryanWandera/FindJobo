from django.shortcuts import render
from findjoboapp.models import *

def home_view(request, city="nairobi" ):

    if request.user.is_authenticated:
        context = {
        "jobs" : Job.objects.filter(city__name=city.lower()) ,
        "selected_city" : city,
        "categories": Category.objects.all(),
        "cities" : City.objects.all()
    }
    else:
        context = {
        "jobs" : Job.objects.filter(city__name=city.lower())[:3] ,
        "selected_city" : city,
        "categories": Category.objects.all(),
        "cities" : City.objects.all()
    }

    
    return render(request, "index.html", context)



def privacy_policy_view(request):

    return render(request, "privacy-policy.html")

def terms_of_service_view(request):

    return render(request, "terms-of-service.html")

def logout_view(request):
    return render(request, "logout-screen.html")