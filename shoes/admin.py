from django.contrib import admin

# Register your models here.
from .models import Shoe,Discription,Kind,Size

class KindAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':['name']}
    list_display = ['name']

# admin.site.register(Discription,DiscriptinAdmin)
admin.site.register(Shoe)
admin.site.register(Discription)
admin.site.register(Kind,KindAdmin)
admin.site.register(Size)
