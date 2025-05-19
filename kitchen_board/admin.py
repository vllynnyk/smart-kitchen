from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from kitchen_board.models import (Cook,
                                  DishType,
                                  Dish,
                                  DishIngredient,
                                  Ingredient)


admin.site.register(DishType)
admin.site.register(Ingredient)


@admin.register(Cook)
class CookAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("position",)
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("position", "years_of_experience",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "Additional info",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "position",
                    "years_of_experience",
                )
            },
        ),
    )


class DishIngredientInline(admin.TabularInline):
    model = DishIngredient
    extra = 1
    autocomplete_fields = ("ingredient",)


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "dish_type")
    search_fields = ("name",)
    list_filter = ("dish_type",)
    inlines = [DishIngredientInline]
