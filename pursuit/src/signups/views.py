from django.shortcuts import render, render_to_response, RequestContext

# Create your views here.

from .forms import SignUpForm

def home(request):

	form = SignUpForm()
	
	return render_to_response('signup.html', locals(), context_instance=RequestContext(request))