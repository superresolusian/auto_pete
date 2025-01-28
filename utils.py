import numpy as np
import random
from scipy.optimize import minimize, linear_sum_assignment
import itertools
import matplotlib.pyplot as plt

def get_this_week_player_costs(this_week, player_costs):
    '''
    Queries master player costs dictionary to get position
    weights for players in this week's squad

    Parameters
    ----------
    this_week : list
        list of strings of player names
    player_costs: dict
        dictionary where keys are player names, values are
        list of tuples of form ('position identifier' cost)

    Returns
    -------
    dict
        dictionary of player costs for only this week's squad
    '''
    
    this_week_player_costs = dict()
    for player in this_week:
        this_week_player_costs[player] = player_costs[player]
    return this_week_player_costs

def dict_to_cost_matrix(player_costs, formation):
    '''
    Create 2D cost matrix of size (n players, n positions)
    where each row represents a different player and each column
    indicates the weight for that player in the position list
    defined by input parameter 'formation'.

    Parameters
    ----------
    player_costs : dict
        dictionary where keys are player names, values are
        list of tuples of form ('position identifier' cost)
        for only the players in this week's squad
    formation : list
        list of strings representing different formations. These
        strings should match the first item in the tuples in the
        player_costs values.

    Returns
    -------
    `numpy.ndarray`
        2D array of size (n players, n positions) representing
        costs for each player in each position
    '''
    
    cost_matrix = []
    for player in player_costs:
        cost_list = []
        for position in formation:
            # each position in formation is a string
            # identifying the position
            for x in player_costs[player]:
                # player_costs[player] is list of
                # tuples of form ('position', cost)
                if x[0]==position:
                    cost_list.append(x[1])
        cost_matrix.append(cost_list)
    return np.array(cost_matrix)

def append_subs_to_cost_matrix(cost_matrix, subs_weights, team_size=7):
    '''
    Adds cells to hold weights for subs onto cost matrix

    Parameters
    ----------
    cost_matrix : `numpy.ndarray`
        2D matrix of size (n players, n positions) containing
        the costs for each player to play in each position
    subs_weights : list

    Returns
    -------

    '''
    n_subs = len(cost_matrix) - team_size
    cost_matrix_with_subs = []
    for i in range(len(cost_matrix)):
        cost_list = list(cost_matrix[i])
        for j in range(n_subs):
            cost_list.append(subs_weights[i])
        cost_matrix_with_subs.append(cost_list)
    return np.array(cost_matrix_with_subs)

def alter_subs_weights(cost_matrix, subs_weights):
    # todo: make sure that goalie have additional sub weight
    n_subs = len(cost_matrix) - 7
    cost_matrix_with_subs = []
    for i in range(len(cost_matrix)):
        cost_list = list(cost_matrix[i])
        for j in range(n_subs):
            cost_list[-(j+1)] = subs_weights[i]
        cost_matrix_with_subs.append(cost_list)
    return np.array(cost_matrix_with_subs)

def convert_lsa_output_to_formation(cm, row_ind, col_ind, this_week, formation_with_subs):
    formation_dict = {'G':[], 'D':[], 'C':[], 'LW':[], 'RW':[], 'F':[], 'S':[]}
    for i in range(len(col_ind)):
        position = formation_with_subs[col_ind[i]]
        player = this_week[i]
        formation_dict[position].append(player)
    formation_dict['cost'] = cm[row_ind, col_ind].sum()
    return formation_dict

def convert_formation_to_list(formation_dict):
    #out_list = [['etsuko']]
    out_list = []
    out_list.append(formation_dict['G'])
    out_list.append(formation_dict['D'])
    out_list.append(formation_dict['C'])
    out_list.append(formation_dict['LW'])
    out_list.append(formation_dict['RW'])
    out_list.append(formation_dict['F'])
    out_list.append(formation_dict['S'])
    return list(np.concatenate(out_list).flat)