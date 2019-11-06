from django import forms

#create account
class NameForm(forms.Form):
    name = forms.CharField(label='Enter name', max_length=50)
    email = forms.CharField(label='Enter SCU email', max_length=50)
    password = forms.CharField(label='Enter password', max_length=50)

#create team
class TeamForm(forms.Form):
	team_name = forms.CharField(label='Enter team name', max_length=50)

#join team
	
	
#submit team progress
class ProgressForm(forms.Form):
	delta_activity_1 = forms.IntegerField(label='Enter progress for activity 1', initial=0)
	delta_activity_2 = forms.IntegerField(label='Enter progress for activity 2', initial=0)
	delta_activity_3 = forms.IntegerField(label='Enter progress for activity 3', initial=0)

#view team progress