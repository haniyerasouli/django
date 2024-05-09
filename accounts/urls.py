from django.urls import path

from accounts import views

urlpatterns=[
    path('',views.ViewRegistration,name='ViewRegistration'),
]