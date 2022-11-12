from auto_pete.players import Player
from auto_pete.team import Team

print("Running auto_pete ...")

# Set up Team & Players
Roses = Team('Roses')

Sian = Player('Sian', 1, 0, 1, 0)
Vicky = Player('Vicky', 0, 1, 2, 2)
Jaz = Player('Jaz', 0, 3, 1, 0)
Jazzie = Player('Jazzie', 1, 0, 0, 0)
Caroline = Player('Caroline', 1, 0, 0, 0)
Helen = Player('Helen', 1, 0, 3, 0)
Christine = Player('Christine', 0, 0, 1, 2)
Keah = Player('Keah', 0, 1.5, 1, 2)
Shafa = Player('Shafa', 0, 0, 2, 1)
Olivia = Player('Olivia', 0, 2, 2, 0)
Mychelle = Player('Mychelle', 4, 1, 0, 1)

Roses.players = [Sian, Vicky, Jaz, Mychelle, Shafa, Helen, Caroline, Keah]
Roses.num_subs = len(Roses.players)-Roses.teamsize

# Calculate Player Costs
player_costs = []
for player in Roses.players:
    player_costs.append(player.player_costs())

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

