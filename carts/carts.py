from shoes.models import Shoe

#سبد خرید و ارتباط با سیشن-----
class Cart:
    def __init__(self,request):
        self.session=request.session

        cart=self.session.get('session_key')
        if 'session_key' not in request.session:
            cart=self.session['session_key']={}
        self.cart=cart
        #----اضافه کردن کفش به سبد خرید
    def add(self, shoe):
        shoe_id=str(shoe.id)

        # shoe_id = str(shoe.id)
        if shoe_id in self.cart:
            pass
        else:
            self.cart[shoe_id] ={'price':str(shoe.price)}
        self.session.modified=True
        #بازگردانی طول سبد خرید------
    def __len__(self):
        return len(self.cart)

    #دریافت کفش ها در سبد خرید-----
    def get_shoes(self):
        shoe_ids=self.cart.keys()
        shoes=Shoe.objects.filter(id__in=shoe_ids)
        return shoes

