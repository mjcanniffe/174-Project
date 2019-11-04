from django.db import models

class Team(models.Model):
	# auto-gen id is primary key (?)
	#team_id already gen (?)
	leader = models.CharField(max_length=50)
	member_2 = models.CharField(max_length=50)
	member_3 = models.CharField(max_length=50)
	team_name = models.CharField(max_length=50)

class User(models.Model):
	# auto-gen id is primary key (?)
	team = models.CharField(max_length=50)
	email = models.CharField(max_length=50)
	hashed_password = models.CharField(max_length=50)
	name = models.CharField(max_length=50)
	#team_id = models.int() #need more parameters?

class Progress(models.Model):
	team = models.ForeignKey(Team)
	activity_1_prog = models.int()
	activity_2_prog = models.int()
	activity_3_prog = models.int()