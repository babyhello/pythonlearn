class Team:
    name = "Normal Team"


team1 = Team()
print(team1.name, Team.name)
team1.name = "R&D team"
print(team1.name, Team.name)
del team1.name
print(team1.name, Team.name)
team1.member = 7
team1.location = 'Taipei'
print(team1.name, team1.member, team1.location)
print(dir(team1))