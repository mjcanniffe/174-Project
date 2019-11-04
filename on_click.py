from polls.models import Team, User, Progress

#create account
user_email=""
hashed_pass=""
user_name=""

new_account = User(email=user_email, hashed_password=hashed_pass, name=user_name)
new_account.save()

#create team
t_name=""
t_leader=""

new_team = Team(leader=t_leader, team_name=t_name)
new_team.save()

#join team
user_name=""
account = User.objects.filter(name=user_name)

t_name=""
team = Team.objects.filter(team_name=t_name)
t_id = team.team_id

account.team_id=t_id
account.save()

if(team.member_2==NULL):
	team.member_2 = account.id
elif(team.member_3==NULL):
	team.member_3 = account.id
	#otherwise, can't add
team.save()

#submit team progress
team_id=""
delta_activity_1 = ""
delta_activity_2 = ""
delta_activity_3 = ""

team = Team.objects.filter(team=team_id)
team.activity_1_prog=team.delta_activity_1+delta_activity_1
team.activity_2_prog=team.delta_activity_2+delta_activity_2
team.activity_3_prog=team.delta_activity_3+delta_activity_3

team.save()

#view team progress
team_id=""
team = Team.objects.filter(team=team_id)
team.activity_1_prog
team.activity_2_prog
team.activity_3_prog