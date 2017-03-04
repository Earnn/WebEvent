from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Person(models.Model):
	"""docstring for Person"""
	name=models.CharField(max_length=100)
	def __unicode__(self):
		return u"%s"%(self.name)

class Image(models.Model):
	"""docstring for Image"""
	image=models.ImageField(upload_to='images')
	description=models.CharField(max_length=100,blank=True,null=True)
		
