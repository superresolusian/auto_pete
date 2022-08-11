from auto_pete.players import Player
from auto_pete.team import Team

print("Running auto_pete ...")

# Set up Team & Players
Roses = Team('Roses')

Sian = Player('Sian', 3, 0, 1, 0)
Vicky = Player('Vicky', 0, 1, 2, 2)
Jaz = Player('Jaz', 0, 2, 1, 0)

Roses.players = [Sian, Vicky, Jaz]
Roses.num_subs = 3


# Calculate Player Costs
player_costs = []
for player in Roses.players:
    player_costs.append(player.player_costs())

team_cost_matrix = Roses.team_cost_matrix()
print('Team Cost Matrix:')
print(team_cost_matrix)
