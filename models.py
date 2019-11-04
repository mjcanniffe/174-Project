from django.db import models

class Team(models.Model):
	# auto-gen id is primary key (?)
	#team_id already gen (?)
	leader = models.ForeignKey(User)
	member_2 = models.ForeignKey(User)
	member_3 = models.ForeignKey(User)
	team_name = models.CharField(max_length=50)

class User(models.Model):
	# auto-gen id is primary key (?)
	team = models.ForeignKey(Team)
	email = models.CharField(max_length=50)
	hashed_password = models.CharField(max_length=50)
	name = models.CharField(max_length=50)
	#team_id = models.int() #need more parameters?

class Progress(models.Model):
	team = models.ForeignKey(Team)
	activity_1_prog = models.int()
	activity_2_prog = models.int()
	activity_3_prog = models.int()