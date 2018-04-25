from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('goals/', views.goals, name='goals'),
    path('<int:task_id>/', views.view_task, name='move'),
]