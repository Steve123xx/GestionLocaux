from django.contrib import admin
from .models import LoginUser,LoginAdmin

class loginUser(admin.ModelAdmin):
    list_display=('UserName','Password')

class loginadmin(admin.ModelAdmin):
    list_display=('AdminName','Password')


admin.site.register(LoginUser,loginUser)
admin.site.register(LoginAdmin,loginadmin)
