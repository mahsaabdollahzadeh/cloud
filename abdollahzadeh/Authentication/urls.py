from django.urls import path
from .import views



urlspatterns=[

    path('',views.Authentication, name='Authentication'),

]