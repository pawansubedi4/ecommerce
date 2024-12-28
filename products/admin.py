from django.contrib import admin
from django.utils.safestring import mark_safe



# Register your models here.
from .models import delevary ,ordersnew ,productsnew,category,storeprofiles,commentbox

@admin.register(delevary)
class delevaryAdmin(admin.ModelAdmin):
    list_display =['dm_name','dm_location','dm_number','image','dm_salary','dm_others','password']

    def image(self,oj):
        if oj.dm_photo:
            return mark_safe(f'<img src="{oj.dm_photo.url}"width="50" height="50">')
        return "no image"
    
@admin.register(ordersnew)
class ordersnewAdmin(admin.ModelAdmin):
    list_display =['o_name','o_price','o_discount','image','o_location','o_number','o_total']

    def image(self,oj):
        if oj.o_photo:
            return mark_safe(f'<img src="{oj.o_photo.url}"width="50" height="50">')
        return "no image"

@admin.register(productsnew)
class productsnewAdmin(admin.ModelAdmin):
    list_display = ['p_name','show_image','p_price','p_discount','p_detail','p_quantity','p_others','category']


    def show_image(self,obj):
        if obj.p_photo:
            return mark_safe(f'<img src="{obj.p_photo.url}"width="50" height="50">')
        return "no image"

@admin.register(category)
class categoryAdmin(admin.ModelAdmin):
    list_display =['c_name','image','c_discount']

    def image(self,oj):
        if oj.c_image:
            return mark_safe(f'<img src="{oj.c_image.url}"width="50" height="50">')
        return "no image"

@admin.register(storeprofiles)
class storeprofilesAdmin(admin.ModelAdmin):
    list_display =['sp_name','sp_location','sp_number','image','sp_salary','sp_others','password']

    def image(self,oj):
        if oj.sp_photo:
            return mark_safe(f'<img src="{oj.sp_photo.url}"width="50" height="50">')
        return "no image"
    
@admin.register(commentbox)
class commentAdmin(admin.ModelAdmin):
    list_display =['name','email','phone_number','comments']  

  