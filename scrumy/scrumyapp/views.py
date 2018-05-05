from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import ScrumyGoals, GoalStatus, ScrumyUser
from .forms import AddUserForm, AddTaskForm, ChangeTaskStatusForm

# Create your views here.
def index(request):
	users = ScrumyUser.objects.all()
	context = {'users': users}
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
			return redirect('scrumy:users')
	else:
		form = AddUserForm()
	context = {'form': form}
	return render(request, 'scrumyapp/adduser.html', context)

def add_task(request):
	if request.method =="POST":
		form = AddTaskForm(request.POST)
		if form.is_valid:
			form.save()
			return redirect('scrumy:users')
	else:
		form = AddTaskForm()
	context = {'form': form}
	return render(request, 'scrumyapp/addtask.html', context)

def get_users(request):
	users = ScrumyUser.objects.all()
	context= {'users': users}
	return render(request, 'scrumyapp/users.html', context)

def change_task_status(request, goal_id):
	if request.method =="POST":
		form = ChangeTaskStatusForm(request.POST)
		if form.is_valid:
			new_status = request.POST.get('status_id')
			status = GoalStatus.objects.get(id=new_status)
			try:
				goal = ScrumyGoals.objects.get(id=goal_id)
			except ScrumyGoals.DoesNotExist:
				raise Http404('There is no goal with the id ' + str(goal_id))
			goal.status_id = status
			# update moved_by field, but this require getting logged in user info
			goal.save()
			return redirect('scrumy:index')
	else:
		form = ChangeTaskStatusForm()
	context = {'form': form}
	return render(request, 'scrumyapp/changestatus.html', context)
'''
def login_user(request):
	if request.method =='POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('scrumy:index')
		else:
			messages.error(request, 'Incorrect username or password')
	context = {}
	return render(request, 'registration/login.html', context)
'''
