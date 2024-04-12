from django.contrib import admin
from .models import Product, Customer, Order, Category
from django import forms
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'stock')


class ProductAdminForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'rows':10, 'cols': 80}))
    class Meta:
        model = Product
        fields = '__all__'

class OrderAdmin(admin.ModelAdmin):
    list_display = ('quantity', 'total_price')

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')



admin.site.register(Product, ProductAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Category, CategoryAdmin)

