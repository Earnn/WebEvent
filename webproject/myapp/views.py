from django.shortcuts import render
from models import Person, Image
# Create your views here.
def home(request):
	return render(request, 'home.html', {'key': "value" })

def base(request):
	return render(request, 'base.html', {'key': "value" })
