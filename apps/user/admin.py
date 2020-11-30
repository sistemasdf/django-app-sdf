from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm,CustomUserCreationForm
from .models import User

# Register your models here.
#admin.site.register(User, UserAdmin)
# Heredamos del UserAdmin original para usar nuestros formularios customizados
class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    fieldsets = UserAdmin.fieldsets + (
        (
            None, {
                'fields': (
                    'weavers',
                    'user_admin',
                )
            }
        ),
    )

@admin.register(User)
class UserAdmin(CustomUserAdmin):
    list_display =  (
        'id',
        'username',
        'password',
        'first_name',
        'last_name',
        'email',
        'is_staff',
        'is_active',
        'is_superuser',
        'weavers',
        'user_admin',
        'last_login',
        'date_joined'
    )
