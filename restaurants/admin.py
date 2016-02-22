from django.contrib import admin

# Register your models here.
from restaurants.models import Restaurant, Food

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'address')
    search_fields = ('name','phone_number')

class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'restaurant', 'price','is_spicy')
    list_filter = ('is_spicy',)
    ordering = ('-price',)
    fields = ('price','restaurant')


admin.site.register(Restaurant,RestaurantAdmin)
admin.site.register(Food,FoodAdmin)