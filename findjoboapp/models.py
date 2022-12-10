from django.db import models
from djrichtextfield.models import RichTextField
from datetime import datetime


class City(models.Model):
    name = models.TextField(max_length=50)

    def save(self, force_insert=False, force_update=False):
        self.name = self.name.lower()
        super(City, self).save(force_insert, force_update)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.TextField(max_length=50)  

    def save(self, force_insert=False, force_update=False):
        self.name = self.name.lower()
        super(Category, self).save(force_insert, force_update)

    
    def __str__(self):
        return self.name


class Job(models.Model):
    
    title = models.TextField(max_length=100, blank=False)
    description = RichTextField()
    company = models.TextField(max_length=50, blank=False)
    company_logo = models.ImageField(blank=False)
    city = models.ForeignKey(City, null=True, blank=True, unique=False, on_delete= models.PROTECT)
    category = models.ForeignKey(Category,null=True, unique=False, blank=True, on_delete= models.PROTECT)
    application_url = models.URLField()
    expiry_date = models.DateField(null=False, blank=False, default=datetime.now)


    def __str__(self):
        return self.title

