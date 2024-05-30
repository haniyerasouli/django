# from PIL.DdsImagePlugin import item
from pkgutil import get_data

import django.urls
from PIL.DdsImagePlugin import item
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from shoes.models import Shoe


# Create your views here.
#viewshoe برای نمایش محصولات
def viewShoe(request):
    shoe_record=Shoe.objects.all()
    return render(request,'shoes/shoe_list.html',{'shoe_record':shoe_record})

#برای نمایش جزییات هر یک از محصولات
def viewShoedetail(request,s,pk):
    shoe_detail=get_object_or_404(Shoe,slug=s,id=pk)
    return render(request,'shoes/shoe_detail.html',{'shoe':shoe_detail})



