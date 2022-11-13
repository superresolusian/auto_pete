from auto_pete.players import Player
from auto_pete.team import Team


def output_formation(team_preferences):

    print('Team Preferences:', team_preferences)

    # Instantiate Team object
    # TODO: add Team Name box to front end
    Roses = Team('Roses')

    # Add Player objects to Team object
    # TODO: below seems clunky
    #  - seek cleaner way of adding Player objects to Team class
    player_list = []
    for p in range(len(team_preferences)):
        player_list.append(Player(
            team_preferences[p][0],
            int(team_preferences[p][1]),
            int(team_preferences[p][2]),
            int(team_preferences[p][3]),
            int(team_preferences[p][4])
        ))

    Roses.players = player_list
    Roses.num_subs = len(Roses.players) - Roses.teamsize

    # Calculate Player Costs
    player_costs = []
    for player in Roses.players:
        player_costs.append(player.player_costs())

    team_cost_matrix = Roses.team_cost_matrix()

    formation_with_subs = Roses.formation.copy()
    for i in range(Roses.num_subs):
        formation_with_subs.append('S')

    formation_output = Roses.cost_matrix_to_formation(team_cost_matrix, Roses.get_player_names(), formation_with_subs)

    return formation_output
