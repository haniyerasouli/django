from django.http import JsonResponse
from django.shortcuts import render,get_object_or_404

from .carts import Cart
from shoes.models import Shoe


#----view cart سبد خرید
def cart(request):
    cart=Cart(request)
    cart_shoes=cart.get_shoes()

    return render(request,'carts/cart.html',{'cart_shoes':cart_shoes})


#----view cart_add اضافه کردن به سبد خرید
def cart_add(request):
    cart=Cart(request)

    if request.POST.get('action') == 'post':
        shoe_id=request.POST.get('shoe_id')

        if shoe_id:
            shoe_id=int(shoe_id)
            shoe=get_object_or_404(Shoe,id=shoe_id)
            cart.add(shoe=shoe)
            cart_quantity=cart.__len__()
            response = JsonResponse({'qty': cart_quantity})
            # response=JsonResponse({'shoe.brand':shoe.brand})
            return response
        else:
            # ارسال پاسخ خطا به کاربر
            return JsonResponse({'error': 'shoe_id is required'}, status=400)