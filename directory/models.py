# -*- coding: utf-8 -*-

from django.db import models
from tagging.fields import TagField
from tagging.models import Tag

class Company(models.Model):
    name = models.CharField('Company name', max_length=200)
    logo = models.ImageField(upload_to='logos', blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    approved = models.BooleanField(default=False)
    
    website = models.URLField(verify_exists=True, blank=True, null=True)
    email = models.EmailField(null=True, blank=True)
    address = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    year = models.CharField('foundation year', max_length=4, blank=True, null=True)
    
    map_lat = models.DecimalField('latitude',max_digits=20, decimal_places=15, blank=True, null=True)
    map_lon = models.DecimalField('longitude', max_digits=20, decimal_places=15, blank=True, null=True)
    
    tags = TagField()
    
    def get_tags(self):
        return Tag.objects.get_for_object(self) 
    
    def __unicode__(self):
        return u'%s' % self.name
    
class Person(models.Model):
    name = models.CharField(max_length=200)
    company = models.ForeignKey(Company)
    position = models.CharField(max_length=200)
    email = models.EmailField(null=True, blank=True)
    website = models.URLField(verify_exists=True, null=True, blank=True)
    twitter = models.CharField('Twitter username',max_length=30,null=True, blank=True)
    linkedin = models.URLField('LinkedIn URL', verify_exists=True, null=True, blank=True)
    
    def __unicode__(self):
        return u'%s' % self.name
    
