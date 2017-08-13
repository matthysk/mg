from django.shortcuts import render, redirect
from django.apps import apps
from django.http import JsonResponse

from . import forms as mgforms
from . import models as mgmodels

# Create your views here.

def index(request):
    '''Not much to do'''
    return render(request, 'mg/index.html')

def create_view(request, model_name):
    ModelClass = apps.get_model(app_label='mg', model_name=model_name)
    formClass = {
            'plantinglocation': mgforms.NewPlantingLocationForm,
            'seedbatch': mgforms.NewSeedBatchForm,
            'planting': mgforms.NewPlantingForm,
            'transplant':  mgforms.NewTransplantForm,
            'variety':  mgforms.NewVarietyForm,
            }[model_name]
    if request.method == 'POST':
        form = formClass(request.POST)
        if form.is_valid():
            item = form.save()
            return redirect(item)
    else:
        form = formClass()
    heading = 'Adding new {}'.format(ModelClass._meta.verbose_name.title())
    return render(request, 'mg/form.html', {'form': form, 'heading': heading})

def list_view(request, model_name):
    ModelClass = apps.get_model(app_label='mg', model_name=model_name)
    items = ModelClass.objects.all()
    return render(
            request, 
            'mg/list.html', 
            {'items': items, 'model_name': model_name},
        )

def detail_view(request, model_name, pk):
    ModelClass = apps.get_model(app_label='mg', model_name=model_name)
    item = ModelClass.objects.get(pk=pk)
    return render(request, 'mg/detail.html', {'item': item})

import base64
from django.core.files.base import ContentFile
import datetime
import pytz

def add_photo(request, model_name, pk):
    ModelClass = apps.get_model(app_label='mg', model_name=model_name)
    item = ModelClass.objects.get(pk=pk)
    if request.is_ajax():
        try:
            photo = mgmodels.Photo()
            photo.dateCreated = datetime.datetime.now(pytz.timezone('Africa/Johannesburg'))
            photo.content_object = item
            encoded_string = request.POST['imageData']
            fileformat, imgstr = encoded_string.split(';base64,')
            ext = fileformat.split('/')[-1]
            decoded = base64.b64decode(imgstr)
            filename = '-'.join([item._meta.model_name, str(item.pk), photo.dateCreated.strftime('%Y-%m-%d-h%Hm%M')]) + '.' + ext
            contentFile = ContentFile(base64.b64decode(imgstr), name=filename)
            photo.photo.save(name=filename, content=contentFile)
            return JsonResponse({"result": "success"})
        except Exception as e:
            print(e)
            raise e
    return render(request, 'mg/add_photo.html', {'item': item})

