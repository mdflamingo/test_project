from django.contrib import admin
from user.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'phone_number',)
    list_display_links = ('pk', 'phone_number')
    search_fields = ('phone_number',)
    list_filter = ('phone_number',)

    empty_value_display = '-пусто-'