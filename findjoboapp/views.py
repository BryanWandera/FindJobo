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



def privacy_policy_view(request):

    return render(request, "privacy-policy.html")

def terms_of_service_view(request):

    return render(request, "terms-of-service.html")