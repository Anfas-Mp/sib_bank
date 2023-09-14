# Register your models here.
from django.contrib import admin
from .models import District,Branch,Person

# Register your models here.
class DistrictAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(District,DistrictAdmin)

class BranchAdmin(admin.ModelAdmin):
    list_display = ['area','slug']
    prepopulated_fields = {'slug':('area',)}
admin.site.register(Branch,BranchAdmin)

admin.site.register(Person)
