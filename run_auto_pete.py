from auto_pete.players import Player
from auto_pete.team import Team

print("Running auto_pete ...")

# Set up Team & Players
Roses = Team('Islington Roses')

Roses.add_player('Sian', [1, 0, 1, 0])
Roses.add_player('Vicky', [0, 1, 2, 2])
Roses.add_player('Jaz', [0, 3, 1, 0])
Roses.add_player('Jazzie', [1, 0, 0, 0])
Roses.add_player('Caroline', [1, 0, 0, 0])
Roses.add_player('Mychelle', [4, 1, 0, 1])
Roses.add_player('Christine', [0, 0, 1, 2])
Roses.add_player('Keah', [0, 1.5, 1, 2])
Roses.add_player('Olivia', [0, 2, 2, 0])

team_cost_matrix = Roses.team_cost_matrix()
print(f'Team Name: {Roses.teamname}')
print(f'Team Cost Matrix:\n {team_cost_matrix}')
print(f'Cost Matrix shape: {team_cost_matrix.shape}')
print(f'Players: {Roses.get_player_names()}')
print(f'Formation + Subs: {Roses.formation}')
print(f'Num Players: {Roses.num_players}')
print(f'Num Subs: {Roses.num_subs}')
print(f'Num Match Periods: {Roses.num_periods}')

output_formation = Roses.cost_matrix_to_formation(team_cost_matrix, Roses.get_player_names(), Roses.formation)
print("Formation", output_formation)

