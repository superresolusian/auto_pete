from app import app

from auto_pete.team import Team


def output_formation(team_preferences):
    """
    Convert team_preferences into a formation
    :param team_preferences: HTML form converted to list of player positional preferences
    :return formation: dictionary of final formation
    """

    app.logger.info(f'Team Preferences:\n {team_preferences}')

    # Instantiate Team object
    # TODO: add Team Name box to front end
    TeamObj = Team('Roses')

    # Add Player objects to Team object
    for player_input in team_preferences:
        player_name = player_input[0]
        # TODO: update TeamObj below to take any number of player_input prefs
        TeamObj.add_player(player_name,
                           [player_input[1],
                            player_input[2],
                            player_input[3],
                            player_input[4]]
                           )

    team_cost_matrix = TeamObj.team_cost_matrix()

    formation = TeamObj.cost_matrix_to_formation(team_cost_matrix,
                                                 TeamObj.get_player_names(),
                                                 TeamObj.formation)

    app.logger.info(f'Team Name: {TeamObj.teamname}')
    app.logger.info(f'Team Cost Matrix:\n {team_cost_matrix}')
    app.logger.info(f'Cost Matrix shape: {team_cost_matrix.shape}')
    app.logger.info(f'Players: {TeamObj.get_player_names()}')
    app.logger.info(f'Formation + Subs: {TeamObj.formation}')
    app.logger.info(f'Num Players: {TeamObj.num_players}')
    app.logger.info(f'Num Subs: {TeamObj.num_subs}')
    app.logger.info(f'Num Match Periods: {TeamObj.num_periods}')
    app.logger.info(f'Formation: {formation}')

    return formation
