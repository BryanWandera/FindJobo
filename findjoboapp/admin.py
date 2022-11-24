from django.contrib import admin
from django.contrib.admin import AdminSite
from findjoboapp.models import Job, Category, City
from django_admin_relation_links import AdminChangeLinksMixin



@admin.register(Job)
class JobAdmin(AdminChangeLinksMixin, admin.ModelAdmin):
    list_display = ['title', 'company', 'city']

class Job(admin.ModelAdmin):
    pass

@admin.register(Category)
class Job(admin.ModelAdmin):
    pass

@admin.register(City)
class Job(admin.ModelAdmin):
    pass


admin.site.site_header = 'FindJobo Command Center'


admin.register(Job)
admin.register(Category)
admin.register(City)
