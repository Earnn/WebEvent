from django.shortcuts import render
from models import Person, Image
# Create your views here.
def home(request):
	image_list = Image.objects.all()

	return render(request, 'home.html', {
			'image_list': image_list,
			
		
			 })

def base(request):
	return render(request, 'base.html', {'key': "value" })
