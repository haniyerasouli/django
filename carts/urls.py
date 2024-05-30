from django.urls import path

from carts import views

urlpatterns=[
    path('',views.cart,name='cart'),
    path('add/',views.cart_add,name='cart_add'),
]