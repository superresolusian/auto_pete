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
