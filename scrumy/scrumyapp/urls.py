from django.urls import path

from . import views

app_name = 'scrumy'

urlpatterns = [
    path('', views.index, name='index'),
    path('dailytask/', views.dailytask_goals, name='dailytask'),
    path('<int:task_id>/', views.move_goal, name='move_goal'),
    path('users/', views.get_users, name='users'),
    path('adduser/', views.add_user, name='add_user'),
    path('addtask/', views.add_task, name='add_task'),
]