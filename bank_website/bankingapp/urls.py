from django.urls import path
from .import views
app_name='bankingapp'

urlpatterns=[
    path('', views.index,name='index'),
    path('new/',views.new,name='new'),
    path('add/',views.person_create_view, name='person_add'),
    path('ajax/load-areas/',views.load_areas, name='ajax_load_areas'),
    path('submit/',views.submit,name='submit'),
]