'''Module 4: Individual Programming Assignment 1
Parsing Data
This assignment covers your ability to manipulate data in Python.
'''
social_graph = {
    "@bongolpoc":{"first_name":"Joselito",
                  "last_name":"Olpoc",
                  "following":[
                  ]
    },
    "@joaquin":  {"first_name":"Joaquin",
                  "last_name":"Gonzales",
                  "following":[
                      "@chums","@jobenilagan"
                  ]
    },
    "@chums" : {"first_name":"Matthew",
                "last_name":"Uy",
                "following":[
                    "@bongolpoc","@miketan","@rudyang","@joeilagan"
                ]
    },
    "@jobenilagan":{"first_name":"Joben",
                   "last_name":"Ilagan",
                   "following":[
                    "@eeebeee","@joeilagan","@chums","@joaquin"
                   ]
    },
    "@joeilagan":{"first_name":"Joe",
                  "last_name":"Ilagan",
                  "following":[
                    "@eeebeee","@jobenilagan","@chums"
                  ]
    },
    "@eeebeee":  {"first_name":"Elizabeth",
                  "last_name":"Ilagan",
                  "following":[
                    "@jobenilagan","@joeilagan"
                  ]
        },
    }
def relationship_status(from_member, to_member, social_graph):
    statuses = {0:'no relationships',
                1:'follower',
                2:'followed by',
                3:'friends'}
    status = 0
    if to_member in social_graph.get('from_member',{}).get('following',[]):
        status += 1
    if from_member in social_graph.get('from_member',{}).get('following',[]):
        status += 2
    return statuses[status]
        
    
relationship_status("@eeebeee", "@joeilagan", social_graph)

import numpy as np
# X
board1 = [
['X','X','O'],
['O','X','O'],
['O','','X'],
]
# X
board2 = [
['X','X','O'],
['O','X','O'],
['','O','X'],
]
# O
board3 = [
['O','X','O'],
['','O','X'],
['X','X','O'],
]
# X
board4 = [
['X','X','X'],
['O','X','O'],
['O','','O'],
]
# O
board5 = [
['X','X','O'],
['O','X','O'],
['X','','O'],
]
# NO WINNER
board6 = [
['X','X','O'],
['O','X','O'],
['X','',''],
]
# NO WINNER
board7 = [
['X','X','O',''],
['O','X','O','O'],
['X','','','O'],
['O','X','','']
]

def tic_tac_toe(board):
    def checkRows(board):
        for row in board:
            if len(set(row)) == 1: # set turns ['X','X','O'] to ['X','O'] and ['X','X','X'] to ['X'] so a length of 1 means that the row wins
                return row[0]
        return 0

    def checkDiagonals(board):
        if len(set([board[i][i] for i in range(len(board))])) == 1:
            return board[0][0]
        if len(set([board[i][len(board)-i-1] for i in range(len(board))])) == 1:
            return board[0][len(board)-1]
        return 0

    for newBoard in [board, np.transpose(board)]: #transposition to check rows, then columns
        result = checkRows(newBoard)
        if result:
            return result
        diag_result = checkDiagonals(board)
        if diag_result:
            return diag_result
    return "NO WINNER"
tic_tac_toe(board6)

legs = {
     ("upd","admu"):{
         "travel_time_mins":10
     },
     ("admu","dlsu"):{
         "travel_time_mins":35
     },
     ("dlsu","upd"):{
         "travel_time_mins":55
     }
}

legs = { # turned into legs_2 to differentiate, idk if this is considered hard-coding...
    ('a1', 'a2'): {
        'travel_time_mins': 10
    },
    ('a2', 'b1'): {
        'travel_time_mins': 10230
    },
    ('b1', 'a1'): {
        'travel_time_mins': 1
    }
}

def eta(first_stop, second_stop, route_map):
    # Since it's one-way and fully enclosed, let's use the first node of leg as a ke, so we can access legs directly in O(1) time from dictionary
    restructurized_route_map = {key[0]:(key[1],value['travel_time_mins']) for key, value in route_map.items()}
    summary_time = 0
    # let's start by setting current node "cursor" to beginning
    current_beginning = first_stop
    # we need to loop no more times than there are legs in the route map
    try:
      for _ in restructurized_route_map:
        current_leg = restructurized_route_map[current_beginning]
        summary_time += current_leg[1]
        if current_leg[0] == second_stop:
          return summary_time
        current_beginning = current_leg[0]
    except Exception:
      raise Exception("Error: problem with provided route map or stops")

eta('a1','b1',legs)