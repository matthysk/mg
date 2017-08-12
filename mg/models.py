from django.db import models

# Create your models here.

class SeedBatch(models.Model):
    batchLabel = models.Charfield(max_length=10)

class SeedTray(models.Model):
    trayLabel = models.Charfield(max_length=10)

class Planting(models.Model):
    tray = models.ForeignKey(SeedTray)
    trayLocation = models.CharField
    seedBatch = models.ForeignKey(SeedBatch)
    date = models.DateFields()
