"""
team
"""
import numpy as np
from scipy.optimize import linear_sum_assignment
from auto_pete.players import Player


class Team:

    def __init__(self, teamname=None):

        self.teamname = teamname
        self.players = None
        self.num_players = 0
        self.num_subs = 0
        self.formation = ['D', 'D', 'C', 'W', 'W', 'F']
        self.team_size = len(self.formation) + 1
        self.cost_matrix = []

    def get_player_names(self):
        return [n.name for n in self.players]

    def add_player(self, player_name: str, pos_pref: list):
        """
        add_player - add Player object to Team object

        :param player_name: Player's name
        :param pos_pref: [List of int or str] Player's position preferences
        :return:
        """

        if self.players is None:
            self.players = []

        if type(player_name) is not str:
            Exception('player_name is not type: str')

        if type(pos_pref[0]) is not int:
            pos_pref = [int(p) for p in pos_pref]

        # TODO: pos_prefs should be any length
        self.players.append(
            Player(player_name, pos_pref)
            )

        # update number of players
        self.num_players = len(self.players)

        # update substitutes
        if self.num_players > self.team_size:
            self.num_subs = self.num_players - self.team_size
            self.formation.append('S')

    def team_cost_matrix(self):
        """
        Create team cost matrix of players' preferred positions
        """

        if self.players is None:
            raise Exception('There are no players in the Team object')

        for player in self.players:
            cost_list = []
            player_costs = player.player_costs()
            for position in self.formation:
                for x in player_costs:
                    if x[0] == position:
                        cost_list.append(x[1])
            self.cost_matrix.append(cost_list)

        self.cost_matrix = np.array(self.cost_matrix)

        if self.num_subs > 0:
            self.cost_matrix = np.pad(self.cost_matrix, ((0, 0), (0, self.num_subs)), 'constant')

        return self.cost_matrix

    def cost_matrix_to_formation(self, cost_matrix, players, formation_with_subs):
        """
        Converts Cost Matrix to Formation dict
        cost_matrix – player position preferences
        players – list of Player objects
        formation_with_subs – list of strings indicating positions, plus subs
        """

        # Calculate LSA
        row_ind, col_ind = linear_sum_assignment(cost_matrix)

        # TODO: make dynamic formation dict
        formation_dict = {'D': [], 'C': [], 'W': [], 'F': [], 'S': []}

        for i in range(len(col_ind)):
            position = formation_with_subs[col_ind[i]]
            player = players[i]
            formation_dict[position].append(player)
        formation_dict['cost'] = cost_matrix[row_ind, col_ind].sum()

        return formation_dict
