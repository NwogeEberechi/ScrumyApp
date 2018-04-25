from django.shortcuts import render
from django.http import HttpResponse
from .models import ScrumyGoals, GoalStatus

# Create your views here.
def index(request):
	return HttpResponse('Hello, world.')

def goals(request):
	goals = ScrumyGoals.objects.filter(status_id=4)
	output = ''
	for goal in goals:
		output += '<p> ' + str(goal) + '</p>'
	return HttpResponse(output)

def view_task(request, task_id):
	goals = ScrumyGoals.objects.filter(task_id=task_id)
	output = ''
	if len(goals) == 0:
		output += '<p> There is no goal with the task_id ' + str(task_id) + '</p>'
	else:
		for goal in goals:
			output += '<p> ' + str(goal) + '</p>'
	return HttpResponse(output)
