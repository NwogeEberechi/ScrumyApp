from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('goals/', views.goals, name='goals'),
    path('<int:task_id>/', views.move_goal, name='move_goal'),
    path('users/', views.get_users, name='users'),
    path('adduser/', views.add_user, name='add_user'),
]