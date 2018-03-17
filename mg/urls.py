from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^?$', views.index, name='mg-home'),
    url(r'^(\w*)/new/', views.create_view, name='mg-create'),#returns list of content with tag
    url(r'^(\w*)/list/', views.list_view, name='mg-list'),#returns list of content with tag
    url(r'^(?P<model_name>\w*)/detail/(?P<pk>\d*)/?$', views.detail_view, name='mg-detail'),#returns list of content with tag
    url(r'^add_photo/(?P<model_name>\w*)/(?P<pk>\d*)/$', views.add_photo, name='mg-add-photo'),#returns list of content with tag
    ]
