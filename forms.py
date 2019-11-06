from django import forms

#create account
class NameForm(forms.Form):
    user_name = forms.CharField(label='Enter name', max_length=50)
    user_password = forms.CharField(label='Enter password', max_length=50)
    user_email = forms.CharField(label='Enter SCU email', max_length=50)

#create team
class TeamForm(forms.Form):
	team_name = forms.CharField(label='Enter team name', max_length=50)

#join team
	
	
#submit team progress
class ProgressForm(forms.Form):
	progress = forms.IntegerField(label='Enter progress')

#view team progress