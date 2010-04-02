# -*- coding: utf-8 -*-

from django.db import models
from django.contrib import admin

# COMPANY

class Company(models.Model):
    name = models.CharField('nome da empresa', max_length=200)
    description = models.TextField('descrição', blank=True, null=True)
    address = models.TextField('address', blank=True, null=True)
    phone = models.CharField('telefone', max_length=20, blank=True, null=True)
    website = models.URLField(verify_exists=True, max_length=200, blank=True, null=True)
    email = models.EmailField(null=True, blank=True)
    year = models.CharField('ano de fundação', max_length=4, blank=True, null=True)
    logo = models.ImageField(upload_to='logos',verbose_name='logótipo', blank=True, null=True)
    
    map_lat = models.DecimalField('latitude',max_digits=20, decimal_places=15, blank=True, null=True)
    map_lon = models.DecimalField('longitude', max_digits=20, decimal_places=15, blank=True, null=True)
    
    def __unicode__(self):
        return u'%s' % self.name
    
    class Meta:
        verbose_name = 'empresa'
    
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'website', 'year')
    search_fields = ('name', 'description')
    
    class Media:
        js = ("js/gmapselect.js",)
admin.site.register(Company, CompanyAdmin)    
    
# PERSON
    
class Person(models.Model):
    name = models.CharField('nome', max_length=200)
    position = models.CharField('cargo', max_length=200)
    email = models.EmailField(null=True, blank=True)
    company = models.ForeignKey(Company)
    
    def __unicode__(self):
        return u'%s' % self.name
    
    class Meta:
        verbose_name = 'pessoa'
    
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'company')
    search_fields = ('name', 'position', 'company')
    
admin.site.register(Person, PersonAdmin) 