from django.contrib import admin

# Register your models here.
from .models import Shoe, Discription, Kind, Size




#برای پر شدن اسلاگ به صورت همزمان با نام ---
#نشان دادن نام به جای رکورد-----
class KindAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':['name']}
    list_display = ['name']

#برای پر شدن اسلاگبا ویژگی وبرند و رنگ و قیمت---
#نشان دادن ویژگی و برند و رنگ و قیمت و جنسیت  به جای رکورد-----
#فیلتر بر اساس قیمت------
class ShoeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':['property','brand','color','price']}
    list_filter = ['price']
    list_display = ['property','brand','color','price','gender']
#نشان دادن سایز به جای رکورد-----
class SizeAdmin(admin.ModelAdmin):
    list_display = ['range']



#
# admin.site.register(Discription,DiscriptinAdmin)
admin.site.register(Shoe,ShoeAdmin)
admin.site.register(Discription)
admin.site.register(Kind,KindAdmin)
admin.site.register(Size,SizeAdmin)


