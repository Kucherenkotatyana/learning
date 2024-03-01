class FootballTeam:

    def __init__(self, name):
        self.name = name
        self.count_of_goals = 0

    def team_goals(self):
        self.count_of_goals += 1
        return self.count_of_goals

    def __gt__(self, other):
        return self.count_of_goals > other.count_of_goals

    def __eq__(self, other):
        return self.count_of_goals == other.count_of_goals


f_team = FootballTeam("Barcelona")
s_team = FootballTeam("Real Madrid")

f_team.team_goals()
s_team.team_goals()
s_team.team_goals()

print(f_team > s_team)
print(f_team == s_team)


def winner(team_1, team_2):

    if team_1 == team_2:
        return f"It's draw! {team_1.count_of_goals}:{team_2.count_of_goals}."
    else:
        if team_1 > team_2:
            return f"'{team_1.name}' is winner! It has {team_1.count_of_goals} goals. And '{team_2.name}' has " \
                   f"{team_2.count_of_goals}!"
        else:
            return f"'{team_1.name}' is looser! It has only {team_1.count_of_goals} goals. And '{team_2.name}' has " \
                   f"{team_2.count_of_goals}! '{team_2.name}' is a winner."


print(winner(f_team, s_team))
