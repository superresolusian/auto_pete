"""
auto_pete.py

Automating football team selection so managers don't have to.

Created by Sian Culley
14/11/2021
"""

import numpy as np
import random
from scipy.optimize import minimize, linear_sum_assignment
import itertools
import matplotlib.pyplot as plt

print("AUTO PETE IS PICKING YO' PLAYERS")

# %%

# set up outfield player dictionaries
# array format: [defender, central, winger, forward]

all_players = dict()

# re-write as preferences
all_players['jazzie'] = [('D', 1), ('C', 0), ('W', 0), ('F', 0)]
all_players['caroline'] = [('D', 1), ('C', 0), ('W', 0), ('F', 0)]
all_players['helen'] = [('D', 1), ('C', 0), ('W', 0), ('F', 0)]
all_players['christine'] = [('D', 0), ('C', 0), ('W', 1), ('F', 2)]
all_players['sian'] = [('D', 3), ('C', 0), ('W', 1), ('F', 0)]
all_players['vicky'] = [('D', 0), ('C', 1), ('W', 2), ('F', 2)]
all_players['keah'] = [('D', 0), ('C', 2), ('W', 1), ('F', 2)]
all_players['shafa'] = [('D', 0), ('C', 0), ('W', 2), ('F', 1)]
all_players['olivia'] = [('D', 0), ('C', 1), ('W', 2), ('F', 0)]
all_players['mychelle'] = [('D', 3), ('C', 1), ('W', 0), ('F', 1)]
all_players['jaz'] = [('D', 0), ('C', 2), ('W', 1), ('F', 0)]

# convert preferences to costs
player_costs = dict()

for player in all_players.keys():
    prefs = all_players[player]

    weights = []
    for x in prefs:
        weight = 1 - (1 / x[1]) if x[1] != 0 else 1.0
        weights.append((x[0], weight))

    player_costs[player] = weights


# %%

def get_this_week_player_costs(this_week, player_costs=player_costs):
    this_week_player_costs = dict()
    for player in this_week:
        this_week_player_costs[player] = player_costs[player]
    return this_week_player_costs


def dict_to_cost_matrix(player_costs, formation):
    cost_matrix = []
    for player in player_costs:
        cost_list = []
        for position in formation:
            for x in player_costs[player]:
                if x[0] == position:
                    cost_list.append(x[1])
        cost_matrix.append(cost_list)

    return np.array(cost_matrix)


def append_subs_to_cost_matrix(cost_matrix, subs_weights):
    n_subs = len(cost_matrix) - 6
    cost_matrix_with_subs = []
    for i in range(len(cost_matrix)):
        cost_list = list(cost_matrix[i])
        for j in range(n_subs):
            cost_list.append(subs_weights[i])
        cost_matrix_with_subs.append(cost_list)
    return np.array(cost_matrix_with_subs)


def alter_subs_weights(cost_matrix, subs_weights):
    n_subs = len(cost_matrix) - 6
    cost_matrix_with_subs = []
    for i in range(len(cost_matrix)):
        cost_list = list(cost_matrix[i])
        for j in range(n_subs):
            cost_list[-(j + 1)] = subs_weights[i]
        cost_matrix_with_subs.append(cost_list)
    return np.array(cost_matrix_with_subs)


def convert_lsa_output_to_formation(cm, row_ind, col_ind, this_week, formation_with_subs):
    formation_dict = {'D': [], 'C': [], 'W': [], 'F': [], 'S': []}
    for i in range(len(col_ind)):
        position = formation_with_subs[col_ind[i]]
        player = this_week[i]
        formation_dict[position].append(player)
    formation_dict['cost'] = cm[row_ind, col_ind].sum()
    return formation_dict


# %%

# build cost matrix
this_week = ['jazzie', 'caroline', 'mychelle', 'sian', 'vicky', 'christine', 'olivia', 'jaz']
# this_week = random.sample(all_players.keys(), 9)

print(this_week)
n_players_this_week = len(this_week)

formation = ['D', 'D', 'C', 'W', 'W', 'F']
formation_with_subs = formation.copy()
for i in range(n_players_this_week - 6):
    formation_with_subs.append('S')

this_week_player_costs = get_this_week_player_costs(this_week)
cm_no_subs = dict_to_cost_matrix(this_week_player_costs, formation)

sub_weight = 1.0  # cost of subbed player getting subbed again
n_repeats = 6  # how many periods to split game into

# %%

initial_subs_weights = np.zeros(n_players_this_week)
cm = append_subs_to_cost_matrix(cm_no_subs, initial_subs_weights)

subs_weights = initial_subs_weights.copy()
for i in range(n_repeats):
    row_ind, col_ind = linear_sum_assignment(cm)
    print(convert_lsa_output_to_formation(cm, row_ind, col_ind, this_week, formation_with_subs))

    for i in range(len(row_ind)):
        if formation_with_subs[col_ind[i]] == 'S':
            subs_weights[i] += sub_weight
    cm = alter_subs_weights(cm, subs_weights)

    # TODO: also alter position weights to maintain position?


# %%

def objective_function(x, cm_no_subs, n_repeats):
    vals = []

    cm = append_subs_to_cost_matrix(cm_no_subs, x)
    subs_weights = x.copy()

    for i in range(n_repeats):
        row_ind, col_ind = linear_sum_assignment(cm)
        formation_dict = convert_lsa_output_to_formation(cm, row_ind, col_ind, this_week, formation_with_subs)
        vals.append(formation_dict['cost'])

        for i in range(len(row_ind)):
            if formation_with_subs[col_ind[i]] == 'S':
                subs_weights[i] += 1.0
        cm = alter_subs_weights(cm, subs_weights)

    val = np.var(vals)
    # print(x, val)

    return val


this_week_player_costs = get_this_week_player_costs(this_week)
cm_no_subs = dict_to_cost_matrix(this_week_player_costs, formation)
# cm = append_subs_to_cost_matrix(cm_no_subs, np.zeros(n_players_this_week))

n_repeats = 0
if n_players_this_week == 7:
    n_repeats = 7
elif n_players_this_week == 8:
    n_repeats = 6
elif n_players_this_week == 9:
    n_repeats = 3

bound = (0, 1)
bounds = []
for i in range(n_players_this_week):
    bounds.append(bound)

res = minimize(objective_function, x0=np.zeros(n_players_this_week), args=(cm_no_subs, n_repeats), bounds=bounds,
               method='SLSQP', options={'eps': 0.1})
print(res)

# %% md

todo:
*set
up
cost
matrix
*follow
through
to
end
of
match
* if later
combinations
are
forbidden, go
back and adjust
sub
weights?
*could
turn
into
a
meta - optimisation
problem, where
you
are
trying
to
optimise
the
inital
subs
weights
per
player
to
minimise
total
cost
to
team
*integrate
small
weight
reduction
to
incentivise
not changing
position
*dynamic
cost
matrix - can
i
prevent
failure
cases
where
algorithm
wastes
all
best
combinations
early
on?

# %%

initial_subs_weights = res.x
cm = append_subs_to_cost_matrix(cm_no_subs, initial_subs_weights)

subs_weights = initial_subs_weights.copy()
for i in range(n_repeats):
    row_ind, col_ind = linear_sum_assignment(cm)
    print(convert_lsa_output_to_formation(cm, row_ind, col_ind, this_week, formation_with_subs))

    for i in range(len(row_ind)):
        if formation_with_subs[col_ind[i]] == 'S':
            subs_weights[i] += sub_weight
    cm = alter_subs_weights(cm, subs_weights)


# %%

def plot_formation(formation, t_start, t_stop):
    # format for formation should be: GK, LB, RB, C, LW, RW, CF, S, S, S
    make_pitch()

    positions_x = [2.5, 1.5, 3.5, 2.5, 0.5, 4.5, 2.5, 6.5, 6.5, 6.5]
    positions_y = [4, 2.8, 2.8, 1.6, 1, 1, 0, 3, 2, 1]

    for i in range(len(formation)):
        plt.annotate(formation[i], (positions_x[i], positions_y[i] + 0.25), color='white', fontsize=14, ha='center')

    plt.plot(positions_x, positions_y, 'o', ms=10, markerfacecolor='red', markeredgecolor='white')

    plt.annotate(f'{t_start} - {t_stop} mins', (3.5, 5), color='white', fontsize=14, ha='center')


def make_pitch():
    plt.figure(figsize=[6, 6])
    plt.xlim([-1, 8])
    plt.ylim([-1, 5.5])
    plt.hlines([4.5, -0.5], -0.5, 5.5, color='white')
    plt.hlines(3.5, 1.5, 3.5, color='white')
    plt.vlines([-0.5, 5.5], -0.5, 4.5, color='white')
    plt.vlines([1.5, 3.5], 3.5, 4.5, color='white')

    plt.plot([2.5], [-0.5], 'o', ms=5, color='w')

    ax = plt.gca()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    ax.set_facecolor('green')

    return ax


# %%

plot_formation(['etsuko', 'jazzie', 'caroline', 'vicky', 'siân', 'christine', 'mychelle', 'olivia', 'jaz', 'pete'], 0,
               8)

# %%

plot_formation(['etsuko', 'jazzie', 'caroline', 'olivia', 'siân', 'jaz', 'mychelle', 'vicky', 'christine', 'pete'], 8,
               16)

# %%

plot_formation(['etsuko', 'jazzie', 'mychelle', 'vicky', 'christine', 'jaz', 'olivia', 'caroline', 'siân', 'pete'], 16,
               25)

# %%

plot_formation(['etsuko', 'caroline', 'siân', 'vicky', 'christine', 'jaz', 'olivia', 'jazzie', 'mychelle', 'pete'], 25,
               33)

# %%

plot_formation(['etsuko', 'caroline', 'jazzie', 'vicky', 'christine', 'siân', 'mychelle', 'olivia', 'jaz', 'pete'], 33,
               41)

# %%

plot_formation(['etsuko', 'caroline', 'jazzie', 'olivia', 'jaz', 'siân', 'mychelle', 'vicky', 'christine', 'pete'], 41,
               50)

