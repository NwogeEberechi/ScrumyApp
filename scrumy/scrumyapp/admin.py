from django.contrib import admin
from .models import ScrumyUser, ScrumyGoals, GoalStatus

# Register your models here.

admin.site.register(ScrumyUser)
admin.site.register(ScrumyGoals)
admin.site.register(GoalStatus)