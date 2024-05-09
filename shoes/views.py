from django.shortcuts import render, get_object_or_404

from shoes.models import Shoe


# Create your views here.
def viewShoe(request):
    shoe_record=Shoe.objects.all()
    return render(request,'shoes/shoe_list.html',{'shoe_records':shoe_record})


def viewShoedetail(request,s):
    shoe_detail=get_object_or_404(Shoe,slug=s)
    return render(request,'shoes/shoe_detail.html',{'shoe_details':shoe_detail})