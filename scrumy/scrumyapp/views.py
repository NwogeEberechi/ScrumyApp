from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import Http404
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.views import generic

from .models import ScrumyGoals, GoalStatus, ScrumyUser
from .forms import AddUserForm, AddTaskForm, ChangeTaskStatusForm

# Create your views here.
class GoalIndexView(generic.ListView):
	template_name = 'scrumyapp/goals.html'

	def get_queryset(self):
		return ScrumyGoals.objects.all()


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
	return render(request, 'scrumyapp/goal.html', context)

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
	if request.user.is_authenticated:
		if request.method =="POST":
			form = AddTaskForm(request.POST)
			if form.is_valid:
				status = request.POST.get('status_id')
				status_obj = GoalStatus.objects.get(id=status)
				task = request.POST.get('task')
				user = request.user
				goal = ScrumyGoals(user_id = user, status_id = status_obj, task=task)
				goal.save()
				return redirect('scrumy:users')
		else:
			form = AddTaskForm()
		context = {'form': form}
		return render(request, 'scrumyapp/addtask.html', context)
	else:
		return HttpResponse('Access denied, log in to access this page')


def get_users(request):
	users = ScrumyUser.objects.all()
	context= {'users': users}
	return render(request, 'scrumyapp/users.html', context)

def change_task_status(request, goal_id):
	message = ''
	# check if user is authenticated
	if request.user.is_authenticated:
		current_user = request.user
		current_user_group = current_user.groups.all()
		if current_user_group : 
			if request.method =="POST":
				form = ChangeTaskStatusForm(request.POST)
				if form.is_valid:
					new_status = request.POST.get('status_id') # status from form
					status_object = GoalStatus.objects.get(id=new_status) # new goalstatus object
					try:
						goal = ScrumyGoals.objects.get(id=goal_id) # goal whose status is to be changed
						goal_status = goal.status_id # current  goal status
					except ScrumyGoals.DoesNotExist:
						raise Http404('There is no goal with the id ' + str(goal_id))
					
					# owner permission
					if str(current_user_group[0]) == 'OWNER':
						goal.status_id = status_object
					
					# admin permission 
					elif str(current_user_group[0]) == 'ADMIN':
						if str(goal_status) == 'DT' and status_object.status == 'V':
							goal.status_id = status_object
						else:
							print('You do not have access to move to this status' )

					# Quality analyst permission
					elif str(current_user_group[0]) == 'QUALITY ANALYST':
						if str(goal_status) == 'V' and status_object.status == 'D':
							goal.status_id = status_object 
						else:
							print('You do not have access to move to this status' )

					# Developer permission
					elif str(current_user_group[0]) == 'DEVELOPER':
						if str(goal_status) == 'WT' and status_object.status == 'DT':
							goal.status_id = status_object 
						else:
							return HttpResponse('You do not have access to move to this status')
					else:
						message += 'You do not have permission to change the goal status'
						return HttpResponse('No permission defined for your group')
						#return render(request, 'scrumyapp/changestatus.html', {'message': message})
					# update moved_by field, but this require getting logged in user info
					goal.save()
					return redirect('scrumy:index')
			else:
				form = ChangeTaskStatusForm()
			context = {'form': form}
			return render(request, 'scrumyapp/changestatus.html', context)
		else:
			print('user does not belong to any group')
			return HttpResponse('user does not belong  to any group')
	else:
		return HttpResponse('Access denied, log in to access this page') # check for the right http status to use

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

