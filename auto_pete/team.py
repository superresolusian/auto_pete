"""
team
"""
import numpy as np


class Team:

    def __init__(self, teamname=None):

        self.teamname = teamname
        self.players = None
        self.formation = ['D', 'D', 'C', 'W', 'W', 'F']
        self.teamsize = len(self.formation)+1
        self.num_subs = 0

        # TODO: auto-update object based on number of Player objects in Team
        # property decorator:
        # https://stackoverflow.com/questions/14916284/in-class-object-how-to-auto-update-attributes

        # if self.players is None:
        #     self.num_players = 0
        #     self.num_subs = 0
        # elif self.players is not None:
        #     self.num_players = len(self.players)
        #     self.num_subs = self.num_players - self.teamsize

    def team_cost_matrix(self):
        """
        Create team cost matrix of players' preferred positions
        """

        if self.players is None:
            raise Exception('There are no players in the Team object')

        cost_matrix = []
        for player in self.players:
            cost_list = []
            player_costs = player.player_costs()
            for position in self.formation:
                for x in player_costs:
                    if x[0] == position:
                        cost_list.append(x[1])
            cost_matrix.append(cost_list)

        cost_matrix = np.array(cost_matrix)

        if self.num_subs > 0:
            cost_matrix = np.pad(cost_matrix, ((0, 0), (0, self.num_subs)), 'constant')

        return cost_matrix
