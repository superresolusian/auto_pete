"""
players
"""


class Player:

    def __init__(self, name=None, pos_prefs=list):

        self.name = name
        self.pref_defender = pos_prefs[0]
        self.pref_central = pos_prefs[1]
        self.pref_winger = pos_prefs[2]
        self.pref_forward = pos_prefs[3]

        self.pref_all = [('D', self.pref_defender),
                         ('C', self.pref_central),
                         ('W', self.pref_winger),
                         ('F', self.pref_forward)]

        self.player_costs = self.set_player_costs()

    def set_player_costs(self):
        """
        Convert player preferences tuple array -> costs tuple array
        """
        if self.pref_all is None:
            raise Exception('The player has no position preferences.')

        self.player_costs = []

        for c in range(0, len(self.pref_all)):
            self.player_costs.append(
                (self.pref_all[c][0],
                 pref_to_cost(self.pref_all[c][1]))
            )

        return self.player_costs


def pref_to_cost(pref):
    """
    Convert single preference score to cost
    """

    cost = 1 - (1 / pref) if pref != 0 else 1.0
    return cost
