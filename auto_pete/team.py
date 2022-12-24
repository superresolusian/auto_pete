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
        self.num_periods = 1
        self.formation = ['D', 'D', 'C', 'W', 'W', 'F']
        self.team_size = len(self.formation) + 1
        self.sub_cost = 1.0
        self.cost_matrix = None

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

        # update match periods
        self.set_num_periods()

    def team_cost_matrix(self):
        """
        Create team cost matrix of players' preferred positions
        """

        if self.players is None:
            raise Exception('There are no players in the Team object')

        if self.cost_matrix is None:
            self.cost_matrix = []

        for player in self.players:

            cost_list = []
            player_costs = player.player_costs
            for position in self.formation:
                for x in player_costs:
                    if x[0] == position:
                        cost_list.append(x[1])
            self.cost_matrix.append(cost_list)

        self.cost_matrix = np.array(self.cost_matrix)

        if self.num_subs > 0:
            self.cost_matrix = np.pad(self.cost_matrix, ((0, 0), (0, self.num_subs)), 'constant')

        return self.cost_matrix

    # def set_team_cost_matrix(self):
    #
    #     if self.cost_matrix is None:
    #         raise Exception('There is no cost_matrix for this Team object.')
    #
    #     sub_cost_array = np.zeros(self.num_players)
    #
    #     for period in range(self.num_periods):
    #         row_ind, col_ind = linear_sum_assignment(self.cost_matrix)
    #
    #         for i in range(len(row_ind)):
    #             if self.formation[col_ind[i]] == 'S':
    #                 sub_cost_array[i] += self.sub_cost
    #
    #         self.cost_matrix = alter_subs_weights(self.cost_matrix, sub_cost_array)


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

    def set_num_periods(self):
        """
        Divide match time into number of periods
        :return:
        """
        # TODO: automate based on self.num_players
        if self.num_players == 8:
            self.num_periods = 4
        elif self.num_players == 9:
            self.num_periods = 3
        else:
            self.num_periods = 7


# def alter_subs_weights(cost_matrix, subs_weights):
#     n_subs = len(cost_matrix) - 6
#     cost_matrix_with_subs = []
#     for i in range(len(cost_matrix)):
#         cost_list = list(cost_matrix[i])
#         for j in range(n_subs):
#             cost_list[-(j+1)] = subs_weights[i]
#         cost_matrix_with_subs.append(cost_list)
#     return np.array(cost_matrix_with_subs)