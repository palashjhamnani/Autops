from django.contrib import admin

# Register your models here.
from django.contrib import admin
from autosys.models import Category, Page, Farm, UserProfile
from autosys.models import LinuxServer, LinuxOperation
from django.contrib.auth.models import User


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ('id', 'name', 'farm', 'type', 'slug', 'serverip', 'loadreqlink', 'linkk', 'loadenable', 'loaddisable')

class LinuxServerAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('servname',)}
    list_display = ('servname', 'farm', 'type', 'slug', 'serverip', 'loadreqlink', 'slink', 'loadenable', 'loaddisable')


class PageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'service', 'result', 'delete')


class LinuxOperationAdmin(admin.ModelAdmin):
    list_display = ('id', 'linuxserver', 'description', 'command', 'ltitle', 'lservice', 'lresult')


class FarmAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('farmname',)}

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'website', 'picture', 'apausername', 'apapassword', 'bewenousername', 'bewenopassword', 'linuxusername', 'linuxpassword', 'lbusername', 'lbpassword')



# Register your models here.

# Update the registeration to include this customised interface
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(Farm, FarmAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(LinuxServer, LinuxServerAdmin)
admin.site.register(LinuxOperation, LinuxOperationAdmin)

