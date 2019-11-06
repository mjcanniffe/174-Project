from django.db import models

class Team(models.Model):
	# auto-gen id is primary key (?)
	#team_id already gen (?)
	team_name = models.CharField(primary_key=True, max_length=50)
	leader = models.CharField(max_length=50)
	member_2 = models.CharField(max_length=50, blank=True)
	member_3 = models.CharField(max_length=50, blank=True)

	def __str__(self):
		return self.team_name

class User(models.Model):
	# auto-gen id is primary key (?)
	email = models.CharField(primary_key=True, max_length=50)
	password = models.CharField(max_length=50)
	team = models.CharField(max_length=50, blank=True)
	#name = models.CharField(max_length=50)
	#team_id = models.int() #need more parameters?

	def __str__(self):
		return self.email

class Progress(models.Model):
	team = models.ForeignKey(Team, on_delete=models.SET_NULL, blank=True)
	activity_1_prog = models.IntegerField()
	activity_2_prog = models.IntegerField()
	activity_3_prog = models.IntegerField()

	def __str__(self):
		return self.team