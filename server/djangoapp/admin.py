from django.contrib import admin
from .models import CarMake, CarModel

# Registering models with their respective admins
admin.site.register(CarMake)
admin.site.register(CarModel)


# CarModelInline class
# Inline class to show CarModels within CarMake admin page
# class CarModelInline(admin.TabularInline):  # or admin.StackedInline
#     model = CarModel
#     extra = 1  # Number of empty CarModel forms to show

# # Admin class for CarMake
# @admin.register(CarMake)
# class CarMakeAdmin(admin.ModelAdmin):
#     list_display = ('name',)
#     inlines = [CarModelInline]  # Show CarModels inline

# # Admin class for CarModel
# @admin.register(CarModel)
# class CarModelAdmin(admin.ModelAdmin):
#     list_display = ('name', 'car_make', 'type', 'year')
#     list_filter = ('type', 'year')

# CarModelAdmin class

# CarMakeAdmin class with CarModelInline

# Register models here
