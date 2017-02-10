##AoC_2016_11.py
import itertools
import sys
from copy import deepcopy
from datetime import datetime
def main():
    print datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    move_tracker = {}
    move_watch = True
    #Example case
    #floors = [['SG', 'SM', 'PG', 'PM'], ['TG','RG','RM','CG','CM'],['TM'],[]]
    floors = [['EG', 'EM', 'DG', 'DM', 'SG', 'SM', 'PG', 'PM'], ['TG','RG','RM','CG','CM'],['TM'],[]]
    #floors = [['HM', 'LM'], ['HG'], ['LG'], []]
    #floors = [['HM', 'HG'], [], [], []]
    elevator = 0
    ini_state = Game_State(floors, elevator, 0)
    move_tracker[hash(''.join(ini_state.current_setup[0])+ '_' + ''.join(ini_state.current_setup[1]) + '_' +''.join(ini_state.current_setup[2])+ '_' +''.join(ini_state.current_setup[3]) + ''.join(str(elevator)))] = 1
    while (move_watch ==True):
        moves1 = len(move_tracker)
        move_tracker = climb_tree(ini_state, move_tracker)
        #clean_tree(ini_state)
        if moves1==len(move_tracker):
            move_watch = False


    #make_moves(ini_state, move_tracker) 
    print_levels(ini_state, 0)
    print datetime.now().strftime('%Y-%m-%d %H:%M:%S')

class Game_State:
    def __init__(self, current_setup, elevator_pos, moves_made):
        self.current_setup = current_setup
        self.elevator_pos = elevator_pos
        self.moves_made = moves_made
        self.move_options = []
        self.moves_remain = True
        self.solution_flag = False
    def add_move (self, new_game_state):
        self.move_options.append(new_game_state)

def climb_tree(game_state, move_tracker):
    if game_state.solution_flag == True:
        return move_tracker
    elif len(game_state.move_options)>0 and game_state.moves_remain == True:
        for n in game_state.move_options:
            move_tracker = climb_tree(n, move_tracker)
        return move_tracker
    elif game_state.moves_remain == True:
        move_tracker = make_moves_eff(game_state, move_tracker)
        return move_tracker
    else: 
        game_state.moves_remain = False
        return move_tracker

def clean_tree(game_state):
    for n in game_state.move_options:
        if n.moves_remain == False:
            game_state.move_options.remove(n)
    for p in game_state.move_options:
        clean_tree(p)

def iterate_levels(game_state, move_tracker):
    results = []
    no_changes = True
    if len(game_state.moves_made)>0 and game_state.moves_remain == True:
        for n in game_state.move_options:
            results.append(iterate_levels(n, move_tracker)[0])
    elif game_state.moves_remain == False:
        return True, move_tracker
    else: 
        make_moves_eff(game_state, move_tracker)
        return False, move_tracker




def print_levels(game_state, levels_traveled):
    if validate_solutions(game_state.current_setup) == True:
        print 'Solved', levels_traveled
    else: 
        for n in game_state.move_options:
            print_levels(n, levels_traveled + 1)
# def find_depths(game_state, move_tracker):
#     if game_state.moves_remain = False:
#         next
#     elif 

def make_moves_eff(game_state, move_tracker):
    move_set = decide_movers(game_state.current_setup, game_state.elevator_pos)
    move_track = move_tracker
    for n in range(len(move_set)):
        for p in [-1, 1]:
            new_move = attempt_move(deepcopy(game_state.current_setup), move_set[n], deepcopy(game_state.elevator_pos), int(game_state.elevator_pos) + p, deepcopy(game_state.moves_made), move_tracker)
            move_track = new_move[1]
            if new_move[0] != False:
                discovered_move = Game_State(new_move[0].current_setup, new_move[0].elevator_pos, new_move[0].moves_made)
                if validate_solutions(new_move[0].current_setup) == True:
                    discovered_move.solution_flag=True
                #print 'Move added to log', discovered_move
                game_state.add_move(discovered_move)
    if len(game_state.move_options)==0:
        game_state.moves_remain = False
        return move_tracker
    else: 
        return move_tracker
        
def make_moves(game_state, move_tracker):
    move_set = decide_movers(game_state.current_setup, game_state.elevator_pos)
    move_track = move_tracker
    for n in range(len(move_set)):
        for p in [-1, 1]:
            #print 'Current Gamestate: ', game_state
            new_move = attempt_move(deepcopy(game_state.current_setup), move_set[n], deepcopy(game_state.elevator_pos), int(game_state.elevator_pos) + p, deepcopy(game_state.moves_made), move_tracker)
            move_track = new_move[1]
            if new_move[0] != False:
                discovered_move = Game_State(new_move[0].current_setup, new_move[0].elevator_pos, new_move[0].moves_made)
                #print 'Move added to log', discovered_move
                game_state.add_move(discovered_move)
                if validate_solutions(new_move[0].current_setup) == True:
                    print new_move[0].moves_made
    if len(game_state.move_options)>0:
        print 'New Node.'
        for r in range(len(game_state.move_options)):
            print 'Options to move from here are', game_state.move_options
            make_moves(game_state.move_options[r], move_tracker)
    else: print game_state.move_options

def attempt_move(gamestate_setup, moving_pieces, elevator_start, elevator_new, moves_made, move_tracker):
    if elevator_new > 3 or elevator_new < 0:
        return False, move_tracker
    elif validate_move(deepcopy(gamestate_setup[elevator_new]), deepcopy(gamestate_setup[elevator_start]), moving_pieces, elevator_new) == True:
        #print 'Setup before move being attempted:', gamestate_setup
        #print 'Here is what will be moved:', moving_pieces
        #print 'The elevator will be moved to floor ', elevator_new, 'from floor ', elevator_start
        #move_tracker.append(hash(frozenset())
        new_node = Game_State(gamestate_setup, elevator_new, moves_made + 1)
        if len(''.join(moving_pieces)) > 2:
            new_node.current_setup[elevator_new].extend(moving_pieces)
        else: new_node.current_setup[elevator_new].append(moving_pieces)
        new_node.current_setup[elevator_new].sort()
        new_node.current_setup[elevator_start] = [x for x in new_node.current_setup[elevator_start] if x not in moving_pieces]
        new_node.current_setup[elevator_start].sort()
        #setup_new[elevator_new].append(elevator_new)
        if validate_solutions(new_node.current_setup) == True:
            #print 'Puzzle Solved! ', new_node.moves_made
            return new_node, move_tracker
        elif  hash(''.join(new_node.current_setup[0])+ '_' + ''.join(new_node.current_setup[1]) + '_' +''.join(new_node.current_setup[2])+ '_' +''.join(new_node.current_setup[3]) + ''.join(str(elevator_new))) in move_tracker and move_tracker[hash(''.join(new_node.current_setup[0])+ '_' + ''.join(new_node.current_setup[1]) + '_' +''.join(new_node.current_setup[2])+ '_' +''.join(new_node.current_setup[3]) + ''.join(str(elevator_new)))]<=moves_made+1:
            #print "We've already tried this move."
            return False, move_tracker
        else: 
            move_tracker[hash(''.join(new_node.current_setup[0])+ '_' + ''.join(new_node.current_setup[1]) + '_' +''.join(new_node.current_setup[2])+ '_' +''.join(new_node.current_setup[3]) + ''.join(str(elevator_new)))] = moves_made + 1
            return new_node, move_tracker
    else:
        #print 'Move Invalid'  
        return False, move_tracker

def valid_floor(proposed_floor):
    microchip_only = True
    for n in range(len(proposed_floor)):
        if proposed_floor[n][1] == 'G':
            microchip_only = False
    for n in range(len(proposed_floor)):
        if proposed_floor[n][1] == 'M':
            if proposed_floor[n][0] + 'G' not in proposed_floor and microchip_only == False:
                return False
    return True

def validate_move(proposed_floor, old_floor, elevator_passengers, elevator_pos):
    old_floor_moved = [x for x in old_floor if x not in elevator_passengers]
    if len(''.join(elevator_passengers)) > 2:
        if elevator_passengers[0][1] == 'G' and elevator_passengers[1][1] == 'M' and elevator_passengers[0][0] != elevator_passengers[1][0]:
            return False
        elif elevator_passengers[1][1] == 'G' and elevator_passengers[0][1] == 'M' and elevator_passengers[0][0] != elevator_passengers[1][0]:
            return False
        else:
            proposed_floor.extend(elevator_passengers) 
            return valid_floor(proposed_floor) * valid_floor(old_floor_moved)   
    else: 
        proposed_floor.append(elevator_passengers)
        return valid_floor(proposed_floor) * valid_floor(old_floor_moved) 



def decide_movers(setup, elevator_pos):
    possible_movers = []
    possible_movers = list(itertools.combinations(setup[elevator_pos], 2)) + setup[elevator_pos]
    return possible_movers

def validate_solutions(setup):
    if len(setup[0]) + len(setup[1]) + len(setup[2]) == 0:
        return True
    else: return False

if __name__=='__main__':
    main()

##Just general pseudo-code thoughts: We basically want to take each current setup and determine all possible moves from that setup. We then want to check that move against 
##a hash table to make sure we haven't tried making it before, then we can make a new branch of the tree containing all possible moves from that point. Then we can return the amount of moves it took to get there to find the min.