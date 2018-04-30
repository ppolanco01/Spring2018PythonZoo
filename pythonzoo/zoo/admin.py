from django.contrib import admin

from .models import Zoo, Exhibit

# Register your models here.


class ZooAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'logoFileName', 'get_absolute_url')

admin.site.register(Zoo, ZooAdmin)

class ExhibitAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'get_absolute_url')

admin.site.register(Exhibit, ExhibitAdmin)
