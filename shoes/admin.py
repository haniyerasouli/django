from django.contrib import admin

# Register your models here.
from .models import Shoe,Discription,Kind,Size

class KindAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':['name']}
    list_display = ['name']


class ShoeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':['property','brand','color','price','gender']}
    list_filter = ['price']
    list_display = ['property','brand','color','price','gender']

class SizeAdmin(admin.ModelAdmin):
    list_display = ['range']


# admin.site.register(Discription,DiscriptinAdmin)
admin.site.register(Shoe,ShoeAdmin)
admin.site.register(Discription)
admin.site.register(Kind,KindAdmin)
admin.site.register(Size,SizeAdmin)
