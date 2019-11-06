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
	def is_team_full(self):
		return strlen(self.member_2)>0 and strlen(self.member_3)>0

class User(models.Model):
	# auto-gen id is primary key (?)
	email = models.CharField(primary_key=True, max_length=50)
	password = models.CharField(max_length=50)
	name = models.CharField(max_length=50)
	team = models.CharField(max_length=50, blank=True)
	#team_id = models.int() #need more parameters?

	def __str__(self):
		return self.email
	def give_team(self):
		return self.team

class Progress(models.Model):
	team = models.ForeignKey(Team, on_delete=models.SET_NULL, blank=True)
	activity_1_prog = models.IntegerField()
	activity_2_prog = models.IntegerField()
	activity_3_prog = models.IntegerField()

	def __str__(self):
		return self.team
	def give_prog_1(self):
		return self.activity_1_prog
	def give_prog_2(self):
		return self.activity_2_prog
	def give_prog_3(self):
		return self.activity_3_prog