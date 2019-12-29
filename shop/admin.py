from django.contrib import admin
from shop.models import User, Product

# Register your models here.
class AdminUser(admin.ModelAdmin):
    list_display=['name','username','num','pword','email']

class AdminProduct(admin.ModelAdmin):
    list_display=['p_name','quantity','image']


admin.site.register(User,AdminUser)
admin.site.register(Product,AdminProduct)