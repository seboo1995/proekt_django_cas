from django.contrib import admin
from .models import Password
# Register your models here.

class PasswordAdmin(admin.ModelAdmin):
    class Meta:
        model = Password
    list_display = ['username','pswd','url','timestamp','last_update','notes','user_id']
    list_filter = ['user_id']

admin.site.register(Password,PasswordAdmin)