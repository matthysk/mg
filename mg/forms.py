from django import forms
from mg import models as mgmodels

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
        model = mgmodels.Transplant
        fields = ('fromLocation', 'toLocation')
