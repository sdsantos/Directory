# -*- coding: utf-8 -*-

from django.db import models
from django.contrib import admin
from tagging.fields import TagField
from tagging.models import Tag

# COMPANY

class Company(models.Model):
    name = models.CharField('nome da empresa', max_length=200)
    logo = models.ImageField(upload_to='logos',verbose_name='logótipo', blank=True, null=True)
    description = models.TextField('descrição', blank=True, null=True)
    website = models.URLField(verify_exists=True, blank=True, null=True)
    email = models.EmailField(null=True, blank=True)
    address = models.TextField('address', blank=True, null=True)
    phone = models.CharField('telefone', max_length=20, blank=True, null=True)
    year = models.CharField('ano de fundação', max_length=4, blank=True, null=True)
    
    map_lat = models.DecimalField('latitude',max_digits=20, decimal_places=15, blank=True, null=True)
    map_lon = models.DecimalField('longitude', max_digits=20, decimal_places=15, blank=True, null=True)
    
    tags = TagField()
    
    def get_tags(self):
        return Tag.objects.get_for_object(self) 
    
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
    company = models.ForeignKey(Company)
    position = models.CharField('cargo', max_length=200)
    email = models.EmailField(null=True, blank=True)
    website = models.URLField(verify_exists=True, null=True, blank=True)
    twitter = models.CharField('Twitter username',max_length=30,null=True, blank=True)
    linkedin = models.URLField('LinkedIn URL', verify_exists=True, null=True, blank=True)
    
    def __unicode__(self):
        return u'%s' % self.name
    
    class Meta:
        verbose_name = 'pessoa'
    
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'company')
    search_fields = ('name', 'position', 'company')
    
admin.site.register(Person, PersonAdmin) 