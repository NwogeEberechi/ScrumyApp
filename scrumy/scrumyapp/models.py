from django.db import models

# Create your models here.
class ScrumyUser(models.Model):
    SCRUMY_USER_ROLE = (
        ('O', 'Owner'),
        ('A', 'Admin'),
        ('Q', 'Quality Analyst'),
        ('D', 'Developer'),
    )
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=10)
    role = models.CharField(max_length=1, choices=SCRUMY_USER_ROLE)

    def __str__(self):
        return (self.firstname + ' ' + self.lastname)

    def get_weekly_goals(self):
        return self.scrumygoals_set.filter(status_id=3)

    def get_daily_goals(self):
        return self.scrumygoals_set.filter(status_id=4)

    def get_verified_goals(self):
        return self.scrumygoals_set.filter(status_id=1)

    def get_done_goals(self):
        return self.scrumygoals_set.filter(status_id=2)

class GoalStatus(models.Model):
    GOAL_STATUS = (
        ('V', 'Verified'),
        ('D', 'Done'),
        ('WT', 'Weekly Task'),
        ('DT', 'Daily Task'),
    )
    name = models.CharField(max_length=255, default='scrumystatus')
    status = models.CharField(max_length=2, choices=GOAL_STATUS)

    def __str__(self):
        return self.status

class ScrumyGoals(models.Model):
    user_id = models.ForeignKey(ScrumyUser, on_delete=models.CASCADE)
    status_id = models.ForeignKey(GoalStatus, on_delete=models.CASCADE)
    task = models.TextField()
    task_id = models.IntegerField(default=0)
    moved_by = models.CharField(max_length=50, default='Not been moved')
    movement_track = models.IntegerField(default=1234)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task




