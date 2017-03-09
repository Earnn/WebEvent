from __future__ import unicode_literals
from django.db import models
from django.forms import ModelForm
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

		
class Event(models.Model):	
	"""docstring for Event"""
	title=models.CharField(max_length=200,blank=False,null=False,default="")
	name=models.CharField(max_length=200,blank=False,null=False)
	message=models.CharField(max_length=1000,blank=False,null=False)
	pic=models.ImageField(upload_to="images/",default="")
	created_event = models.DateTimeField(auto_now_add=True)

class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')
	
class Upload(models.Model):
    pic = models.ImageField("Image", upload_to="images/")    
    upload_date=models.DateTimeField(auto_now_add =True)
		
class UploadForm(ModelForm):
    class Meta:
        model = Event
        fields = [
			"title",
			"pic",
			"message",
			"name"
        ]