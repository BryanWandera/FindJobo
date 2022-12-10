
from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from findjoboapp.views import *
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),
    path('<str:city>/', home_view),
    path('<str:city>/<str:category>', home_view),
    path('djrichtextfield/', include('djrichtextfield.urls')),
    path('accounts/', include('allauth.urls')),
    path('privacy-policy', privacy_policy_view),
    path('terms-of-service', terms_of_service_view),
    path('logout-user', logout_view)
    
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

