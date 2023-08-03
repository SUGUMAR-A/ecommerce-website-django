from django.contrib import admin
from .models import *
# Register your models here.
# class catagoryadmin(admin.ModelAdmin):

#     list_display=('name','image','description')
#     admin.site.register(catagory,catagoryadmin)

admin.site.register(catagory)
admin.site.register(product)