from django.contrib import admin
from farmers.models import Farmer, Farm, Crop, Livestock, Price, Receipt

admin.site.register(Farmer)
admin.site.register(Crop)
admin.site.register(Price)
admin.site.register(Livestock)
admin.site.register(Farm)
admin.site.register(Receipt)