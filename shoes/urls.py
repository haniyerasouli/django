from django.urls import path

from shoes import views

urlpatterns=[ path('',views.viewShoe,name='viewShoe'),
    path('<slug:s>',views.viewShoedetail,name='viewShoedetail'),
              ]