from django.shortcuts import render
from django.http import HttpResponse
from .models import ScrumyGoals 

# Create your views here.
def index(request):
	return HttpResponse('Hello, world.')

def goals(request):
	goals = ScrumyGoals.objects.all()
	html = ''
	for goal in goals:
		html += '<p> ' + str(goal) + '</p>'
	return HttpResponse(html)
