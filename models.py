import datetime
from django.db import models
from django.utils import timezone

"""
class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	
	def __str__(self):
		return self.question_text

	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
	

	def __str__(self):
		return self.choice_text
"""



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
	team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True)
	activity_1_prog = models.IntegerField()
	activity_2_prog = models.IntegerField()
	activity_3_prog = models.IntegerField()
