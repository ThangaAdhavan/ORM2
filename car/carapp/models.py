from django.db import models # type: ignore
from django.contrib import admin # type: ignore
class Car(models.Model):
    car_brand = models.CharField()
    car_model = models.CharField()
    car_manufacturedate = models.DateField()
    car_colour = models.CharField()
    car_fc = models.DateField()
    car_fueltype = models.CharField()

class CarAdmin(admin.ModelAdmin):
    list_display = ('car_brand', 'car_model', 'car_manufacturedate', 'car_colour', 'car_fc', 'car_fueltype') 