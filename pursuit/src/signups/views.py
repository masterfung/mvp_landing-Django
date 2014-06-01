from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect
from django.contrib import messages

# Create your views here.

from .forms import SignUpForm

def home(request):

	form = SignUpForm(request.POST or None)

	if form.is_valid():
		save_it = form.save(commit=False)
		save_it.save()
		messages.success(request, 'Putin Berry thanks you and awaits you on the other side.')
		return HttpResponseRedirect('/thank-you/')

	return render_to_response('signup.html', locals(), context_instance=RequestContext(request))

def thankyou(request):

	return render_to_response('thankyou.html', locals(), context_instance=RequestContext(request))
	
def aboutus(request):

	return render_to_response('aboutus.html', locals(), context_instance=RequestContext(request))