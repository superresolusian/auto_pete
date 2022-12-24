from auto_pete.players import Player
from auto_pete.team import Team

print("Running auto_pete ...")

# Set up Team & Players
Roses = Team('Roses')

Roses.add_player('Sian', [1, 0, 1, 0])
Roses.add_player('Vicky', [0, 1, 2, 2])
Roses.add_player('Jaz', [0, 3, 1, 0])
Roses.add_player('Jazzie', [1, 0, 0, 0])
Roses.add_player('Caroline', [1, 0, 0, 0])
Roses.add_player('Mychelle', [4, 1, 0, 1])

# # Calculate Player Costs
# player_costs = []
# for player in Roses.players:
#     player_costs.append(player.player_costs())

team_cost_matrix = Roses.team_cost_matrix()
print('Team Cost Matrix:')
print(team_cost_matrix)
print('Cost Matrix shape:', team_cost_matrix.shape)
print('Players:', Roses.get_player_names())

print('Formation:', Roses.formation)
print('Num Subs:', Roses.num_subs)

formation_with_subs = Roses.formation.copy()
for i in range(Roses.num_subs):
    formation_with_subs.append('S')

print('Formation + Subs:', formation_with_subs)

output_formation = Roses.cost_matrix_to_formation(team_cost_matrix, Roses.get_player_names(), formation_with_subs)
print("Formation", output_formation)

