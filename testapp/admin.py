from django.contrib import admin
from .models import Package, Test

class PackageAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Package, PackageAdmin)


class TestAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'package', 'price', 'created', 'updated']
    list_filter = ['created', 'updated', 'package']
    list_editable = ['price']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Test, TestAdmin)
