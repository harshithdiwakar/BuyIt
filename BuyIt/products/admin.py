from django.contrib import admin
from .models import Product, Shop

class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__','slug']
    class Meta:
        model = Product


class ShopAdmin(admin.ModelAdmin):
    list_display = ['__str__','slug']
    class Meta:
        model = Shop


admin.site.register(Product,ProductAdmin)
admin.site.register(Shop,ShopAdmin)
# admin.site.register(Shop)