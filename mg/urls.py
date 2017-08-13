from django.conf.urls import patterns, include, url

urlpatterns = patterns('mg.views',
    url(r'^/?$', 'index', name='mg-home'),
    url(r'^(\w*)/new/', 'create_view', name='mg-create'),#returns list of content with tag
    url(r'^(\w*)/list/', 'list_view', name='mg-list'),#returns list of content with tag
    url(r'^(?P<model_name>\w*)/detail/(?P<pk>\d*)/?$', 'detail_view', name='mg-detail'),#returns list of content with tag
    url(r'^add_photo/(?P<model_name>\w*)/(?P<pk>\d*)/$', 'add_photo', name='mg-add-photo'),#returns list of content with tag
)
