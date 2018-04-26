from django.shortcuts import render
from django.http import HttpResponse
from .models import ScrumyGoals, GoalStatus

# Create your views here.
def index(request):
	goals = ScrumyGoals.objects.all()
	context = {'goals': goals}
	return render(request, 'scrumyapp/index.html', context)

def goals(request):
	statusDT = GoalStatus.objects.get(status='DT')
	goals = statusDT.scrumygoals_set.all()
	context = {'goals': goals}
	#goals = ScrumyGoals.objects.filter(status_id=4)
	return render(request, 'scrumyapp/goals.html', context)

def view_task(request, task_id):
	goals = ScrumyGoals.objects.filter(task_id=task_id)
	context = {'goals':goals, 'task_id':task_id}
	return render(request, 'scrumyapp/dailytask.html', context)
