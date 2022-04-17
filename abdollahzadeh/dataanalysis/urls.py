from django.urls import path
from .import views



urlspatterns=[

    path('',views.dataanalysis, name='dataanalysis'),

]