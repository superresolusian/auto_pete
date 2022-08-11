"""
players
"""


class Player:

    def __init__(self, name=None, pref_defender=None, pref_central=None, pref_winger=None, pref_forward=None):

        self.name = name
        self.pref_defender = pref_defender
        self.pref_central = pref_central
        self.pref_winger = pref_winger
        self.pref_forward = pref_forward

        self.pref_all = [('D', self.pref_defender),
                         ('C', self.pref_central),
                         ('W', self.pref_winger),
                         ('F', self.pref_forward)]

    def player_costs(self):
        """
        Convert player preferences to costs
        """

        costs = []
        for c in self.pref_all:
            cost = 1 - (1 / c[1]) if c[1] != 0 else 1.0
            costs.append((c[0], cost))

        return costs
