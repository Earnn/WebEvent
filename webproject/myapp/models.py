from __future__ import unicode_literals
from django.db import models
from django.forms import ModelForm, Textarea,TextInput
from django.contrib.auth.models import User
from polls.models import Poll,Choice
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
	title=models.CharField(max_length=200,blank=True,null=True,default="")
	username= models.ForeignKey(User,null=True)
	content=models.CharField(max_length=1000,blank=False,null=False)
	pic=models.ImageField(upload_to="images/",default="")
	created_event = models.DateTimeField(auto_now_add=True)
	date=models.DateField(blank=True,null=True)
	time=models.DateField(blank=True,null=True)

	
class Upload(models.Model):
    pic = models.ImageField("Image", upload_to="images/")    
    upload_date=models.DateTimeField(auto_now_add =True)
		
class UploadForm(ModelForm):
    class Meta:
        model = Event
        fields = [
			"title",
			"content",
			"pic",
			
        ]
       	widgets = {
            'content': Textarea(attrs={'cols': 70, 'rows': 10}),
            'title': TextInput(attrs={'class': 'form-control'}),
           

        }
 

class UpPolls(ModelForm):
    class Meta:
        model = Poll
        fields = [
			"question",
			
        ]
       	widgets = {          
            # 'choice': TextInput(attrs={'class': 'form-control','id':'ch','name':'ch'}),
            'question': TextInput(attrs={'class': 'form-control','id':'titleId','name':'titleId'})
           
}

class UpChoice(ModelForm):
    class Meta:
        model = Choice
        exclude = ('poll',)
        fields = [
			"choice_text",
			
        ]

       	widgets = {          
            'choice_text': TextInput(attrs={'class': 'form-control','id':'ch1','name':'ch1'}),
            # 'poll': TextInput(attrs={'class': 'form-control','id':'titleId','name':'titleId'}),
           
}
               