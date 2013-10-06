# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def Home(request):
	#return HttpResponse('Aloha!')

	return render(request, 'dashboard/aloha.html')

@login_required
def SayMyName(request, called_name = None):

	if called_name != None:

		return render(request, 'dashboard/content_aloha.html', { 'name': called_name, 'gender': 'male', 'BASE_URL': request.get_host() })

	else:

		return redirect('/server/say_my_name/Heisenberg')

