from django.shortcuts import render
from models import Person, Image, Event
from myapp.forms import EventForm
import json
from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from models import UploadForm,Upload
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.context_processors import csrf
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
# Create your views here.
def home(request):
	image_list = Image.objects.all()
	event_list = Event.objects.all()
	# if request.method=="POST":
	# 	query = request.POST.get("q")
	# 	print query
	# 	if query :
	# 		event_list = event_list.filter(
	# 			Q(title__icontains = query)|
	# 			Q(content__icontains = query)
	# 			).distinct()
			
	# 		print "home"
	# 		print event_list
	# 	return HttpResponseRedirect('/search/%s/' % event_list)
		# return HttpResponseRedirect(reverse('search.html', args=[query]))

	
	print event_list
	print image_list
	return render(request, 'home.html', 
		{'event_list': event_list,'image_list' : image_list
		})
		

def base(request):
	return render(request, 'base.html', {'key': "value" })

def searchEvent(request):
	queryset_list = Event.objects.all()
	print queryset_list

	query = request.GET.get("q")
	if query:
		queryset_list = queryset_list.filter(
			Q(title__icontains = query) |
			Q(content__icontains = query) 
			).distinct()
		# queryset_list = queryset_list.filter(title__icontains = query)
	# results = BlogPost.objects.annotate(search=SearchVector('title', 'username', 'content','created_event'),
	# 	).filter(search=your_search_query)
	print queryset_list
	return render(request, 'search.html', {
			'results_search': queryset_list,
			 })


# def searchEvent(request):
#     queryset = Event.objects.all()
#     paginator = Paginator(queryset, 5) # Show 25 contacts per page

#     page = request.GET.get('page')

#     print queryset
#     contacts = {
#     "object_list":queryset,
#     "title": "List",
#     }

#     return render(request, 'search.html', {'contacts': contacts})
	# def addEvent(request): 
# 	if request.method == 'POST':
# 		img = UploadForm(request.POST, request.FILES)
# 		if img.is_valid():
# 			img.save()           
      
# 		print request;
# 		print "request.bod: %s"%request.body;
# 		a=json.loads(request.body)
# 		print a 
# 		print type(a)
# 		print a['msg'];
# 		print a['name'];
# 		s = Event(name=a['name'],message=a['msg'],pic=img);
# 		if s:
# 			s.save();
# 			print "valid";
# 			return HttpResponseRedirect('/')
# 	else:
# 		 images=Upload.objects.all()
# 		 img=UploadForm()
# 	return render(request, 'addEvent.html',{'images':images})
   
class UpdateEventView(UpdateView):
	queryset = Event.objects.all()
	template_name='addEvent.html'
	form_class = UploadForm
	success_url = '/'

class ListEventView(ListView):
    model = Event
    template_name='event_list.html'	

def UploadImg(request):
    if request.method=="POST":
        event = UploadForm(request.POST, request.FILES)       
        if event.is_valid():
            event.save() 
            print "success" 
            print request.user.username
            return HttpResponseRedirect('/')
    else:
        event=UploadForm()
    images=Upload.objects.all()
    return render(request,'addEvent.html',{'form':event,'images':images,'username': request.user.username})	
  

def auth(request):

	
	pwd = request.POST.get('Password','')
	usern = request.POST.get('Username','')

	user = authenticate(username=usern, password=pwd)
	print usern
	print pwd

	
	if user is not None:
		login(request, user)
		u = user
		return HttpResponseRedirect("/")
	else:
		return render(request, 'sssss.html', {'key': "value" })

# def loggedin(request):
# 	return render_to_response(request, 'home.html', {'user': request.user.username })

def log_out(request):
	logout(request)
	return HttpResponseRedirect("/")	