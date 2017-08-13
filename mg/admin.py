from django.contrib import admin
from mg import models

# Register your models here.
admin.site.register(models.PlantingLocation)
admin.site.register(models.SeedBatch)
admin.site.register(models.Planting)
admin.site.register(models.Transplant)
admin.site.register(models.Variety)
