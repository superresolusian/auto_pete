from auto_pete.players import Player
from auto_pete.team import Team

print("Running auto_pete ...")

Roses = Team('Roses')

Sian = Player('Sian', 3, 0, 1, 0)
Vicky = Player('Vicky', 0, 1, 2, 2)
Jaz = Player('Jaz', 0, 2, 1, 0)

Roses.players = [Sian, Vicky, Jaz]

for player in Roses.players:
    print(player.name)
    print(player.pref_all)
    print(player.player_weights())

print(Roses.players)
print(len(Roses.players))
print(Roses.num_subs)
print(Roses.num_players)

# cost_matrix = Roses.