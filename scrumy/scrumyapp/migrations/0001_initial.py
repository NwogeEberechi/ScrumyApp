# Generated by Django 2.0.4 on 2018-04-24 22:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoalStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='scrumystatus', max_length=255)),
                ('status', models.CharField(choices=[('V', 'Verified'), ('D', 'Done'), ('WT', 'Weekly Task'), ('DT', 'Daily Task')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='ScrumyGoals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.TextField()),
                ('task_id', models.IntegerField(default=0)),
                ('moved_by', models.CharField(default='Not been moved', max_length=50)),
                ('movement_track', models.IntegerField(default=1234)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('status_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scrumyapp.GoalStatus')),
            ],
        ),
        migrations.CreateModel(
            name='ScrumyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=10)),
                ('role', models.CharField(choices=[('O', 'Owner'), ('A', 'Admin'), ('Q', 'Quality Analyst'), ('D', 'Developer')], max_length=1)),
            ],
        ),
        migrations.AddField(
            model_name='scrumygoals',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scrumyapp.ScrumyUser'),
        ),
    ]
