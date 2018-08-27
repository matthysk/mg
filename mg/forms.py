from django import forms
from mg import models as mgmodels
from datetimewidget.widgets import DateTimeWidget

class NewPlantingLocationForm(forms.ModelForm):
    class Meta:
        model = mgmodels.PlantingLocation
        fields = ('location',)

class NewSeedBatchForm(forms.ModelForm):
    class Meta:
        model = mgmodels.SeedBatch
        fields = ('variety', 'source')


class NewVarietyForm(forms.ModelForm):
    class Meta:
        model = mgmodels.Variety
        fields = ('species', 'variety')

class NewTransplantForm(forms.ModelForm):
    class Meta:
        model = mgmodels.Transplant
        fields = ('fromLocation', 'toLocation')

class NewPlantingForm(forms.ModelForm):
    class Meta:
        model = mgmodels.Planting
        dateTimeOptions = {
                'format': 'yyyy-mm-dd HH:ii:ss',
                'startView': 1,
                'todayBtn': 'true',
            }
        fields = ('seedBatch', 'location', 'amount', 'plantedTime')
        widgets = {
                'plantedTime': DateTimeWidget(options=dateTimeOptions, bootstrap_version=3)
            }

class PhotoForm(forms.ModelForm):
    class Meta:
        model = mgmodels.Photo
        fields = ('photo',)

