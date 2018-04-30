from django.shortcuts import render, redirect
from django.http import Http404
from .models import ScrumyGoals, GoalStatus, ScrumyUser
from .forms import AddUserForm

# Create your views here.
def index(request):
	goals = ScrumyGoals.objects.all()
	user = ScrumyUser.objects.get(id=1)
	statusWT = GoalStatus.objects.get(status='WT')
	user_goals = statusWT.scrumygoals_set.filter(user_id=1)
	context = {'goals': goals, 'user': user, 'user_goals':user_goals}
	return render(request, 'scrumyapp/index.html', context)

def dailytask_goals(request):
	statusDT = GoalStatus.objects.get(status='DT')
	goals = statusDT.scrumygoals_set.all()
	context = {'goals': goals}
	return render(request, 'scrumyapp/dailytask.html', context)

def move_goal(request, task_id):
	try:
		goals = ScrumyGoals.objects.get(task_id=task_id)
	except ScrumyGoals.DoesNotExist:
		raise Http404('There is no goal with the task_id ' + str(task_id))
	context = {'goals':goals, 'task_id':task_id}	
	return render(request, 'scrumyapp/goals.html', context)

def add_user(request):
	if request.method == "POST":
		form = AddUserForm(request.POST)
		if form.is_valid:
			form.save()
			return redirect('users')
	else:
		form = AddUserForm()
	context = {'form': form}
	return render(request, 'scrumyapp/adduser.html', context)

def get_users(request):
	users = ScrumyUser.objects.all()
	context= {'users': users}
	return render(request, 'scrumyapp/users.html', context)
