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

    def player_weights(self):
        """
        Convert player preferences to weights
        """

        weights = []
        for w in self.pref_all:
            weight = 1 - (1 / w[1]) if w[1] != 0 else 1.0
            weights.append((w[0], weight))

        return weights
