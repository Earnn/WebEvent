from django import forms
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.forms.extras.widgets import SelectDateWidget
from django.contrib.admin import widgets
import datetime
from .models import Person,Event,Image
from django import forms


class EventForm(forms.Form):
	name = forms.CharField()
	message = forms.CharField(widget=forms.Textarea)
   

class PersonForm(ModelForm):
	class Meta:
		model =  Person
		exclude=[]

		widgets = {
			'dob': forms.DateInput(
				attrs={
				'type': 'date', 
				'value': datetime.datetime.now().strftime("%Y-%m-%d")
				}, format="%Y-%m-%d"
			),
		}
		
	def __init__(self, *args, **kwargs):
		super(PersonForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.add_input(Submit('submit', 'Submit'))
		
class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file',
    )