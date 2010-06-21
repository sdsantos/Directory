from django.contrib import admin
from models import *

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'website', 'year', 'approved')
    list_editable = ('approved',)
    search_fields = ('name', 'description')
    
    class Media:
        js = ("js/gmapselect.js",)
        
admin.site.register(Company, CompanyAdmin)  


class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'company')
    search_fields = ('name', 'position', 'company')
    
admin.site.register(Person, PersonAdmin) 