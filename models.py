from django.db import models

class Team(models.Model):
	# auto-gen id is primary key (?)
	#team_id already gen (?)
	team_name = models.CharField(primary_key=True, max_length=50)
	leader = models.CharField(max_length=50)
	member_2 = models.CharField(max_length=50, null=True)
	member_3 = models.CharField(max_length=50, null=True)

class User(models.Model):
	# auto-gen id is primary key (?)
	email = models.CharField(primary_key=True, max_length=50)
	password = models.CharField(max_length=50)
	team = models.CharField(max_length=50, null=True)
	#name = models.CharField(max_length=50)
	#team_id = models.int() #need more parameters?

class Progress(models.Model):
	team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True)
	activity_1_prog = models.IntegerField()
	activity_2_prog = models.IntegerField()
	activity_3_prog = models.IntegerField()