from apps.models import Category, Product, User
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    pass


@admin.register(User)
class UserModelAdmin(UserAdmin):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "email", "password1", "password2"),
            },
        ),
    )


@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    pass
