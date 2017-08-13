from django.db import models

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation

from django.core.urlresolvers import reverse

# Create your models here.

class Photo(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
    photo = models.ImageField(upload_to='mg/%Y/')
    dateCreated = models.DateTimeField()
    class Meta:
        ordering = ['dateCreated']

    def __str__(self):
        return 'Photo of {} taken on {}'.format(self.content_object, self.dateCreated)


class MGMixin(object):
    
    def get_absolute_url(self):
        return reverse('mg-detail', kwargs={'pk': self.pk, 'model_name': self._meta.model_name})

    def field_pairs(self):
        return [ (f.name, getattr(self, f.name),) for f in self._meta.fields ]

    def class_display(self):
        return self._meta.verbose_name

    def model_name(self):
        return self._meta.model_name

class Variety(models.Model, MGMixin):
    species = models.CharField(max_length=40)
    variety = models.CharField(max_length=100, blank=True)
    dateCreated = models.DateTimeField(auto_now_add=True)
    photos = GenericRelation('Photo')
    def __str__(self):
        return self.species + ' - ' + self.variety

class SeedBatch(models.Model, MGMixin):
    SOURCES = (('Collected', 'Collected'),
                ('Living Seeds', 'Living Seeds'),
                ('Stark Ayres', 'Stark Ayres'),
                ('Mayford', 'Mayford'),
                ('Kirchoffs', 'Kirchoffs'),
                ('GardenMaster', 'GardenMaster'),
                )
    label = models.CharField(max_length=10, blank=True)
    source = models.CharField(max_length=20, 
            choices=SOURCES)
    variety = models.ForeignKey('Variety')
    dateCreated = models.DateTimeField(auto_now_add=True)
    photos = GenericRelation('Photo')

    def __str__(self):
        return self.label
    
    def save(self, *args, **kwargs):
        if self.label is None or self.label == '':
            prefix = ''
            for char in self.source:
                if char.isupper():
                    prefix = prefix + char
            number = SeedBatch.objects.filter(source=self.source).count() + 1
            self.label = prefix + str(number)
        super(SeedBatch, self).save(*args, **kwargs)


class Planting(models.Model, MGMixin):
    seedBatch = models.ForeignKey(SeedBatch)
    location = models.ForeignKey('PlantingLocation')
    amount = models.IntegerField()
    plantedTime = models.DateTimeField()
    photos = GenericRelation('Photo')
    dateCreated = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.seedBatch.label + ' -> ' + self.location.location

class Transplant(models.Model, MGMixin):
    seedBatch = models.ForeignKey(SeedBatch)
    amount = models.IntegerField()
    fromLocation = models.ForeignKey('PlantingLocation', related_name='transplantsOut')
    toLocation = models.ForeignKey('PlantingLocation', related_name='transplantsIn')
    photos = GenericRelation('Photo')
    dateCreated = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.fromLocation.location + ' -> ' + self.toLocation.location + '({})'.format(self.dateCreated)

class PlantingLocation(models.Model, MGMixin):
    location = models.CharField(max_length=100)
    photos = GenericRelation('Photo')
    dateCreated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Planting Location'

    #def get_absolute_url(self):
    #    return reverse('mg-detail', self.
    
    def __str__(self):
        return self.location
