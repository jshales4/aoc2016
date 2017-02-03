##AoC_2016_11.py
import itertools
import pdb
from copy import deepcopy
def main():
    move_tracker = {}
    #Example case
    #floors = [['SG', 'SM', 'PG', 'PM'], ['TG','RG','RM','CG','CM'],['TM'],[]]
    floors = [['HM', 'LM'], ['HG'], ['LG'], []]
    elevator = 0
    ini_state = Game_State(floors, elevator, 0)
    make_moves(ini_state, move_tracker) 
    

    # moves = decide_movers(floors, 0)
    # for n in range(len(moves)):
    #     result = attempt_move(deepcopy(ini_state.current_setup), moves[n], ini_state.elevator_pos, 1, ini_state.moves_made, move_tracker)
    #     if result[0] != False:
    #         ini_state.add_move(result[0])
    #         print ini_state.move_options
    #My data
    #floors = [['SG', 'SM', 'PG', 'PM'], ['TG','RG','RM','CG','CM'],['TM'],[]]
    
    #decide_movers(floors, 0)
    ##print make_moves(ini_state, move_tracker)

class Game_State:
    def __init__(self, current_setup, elevator_pos, moves_made):
        self.current_setup = current_setup
        self.elevator_pos = elevator_pos
        self.moves_made = moves_made
        self.move_options = []
    def add_move (self, new_game_state):
        self.move_options.append(new_game_state)

def make_moves(game_state, move_tracker):
    move_set = decide_movers(game_state.current_setup, game_state.elevator_pos)
    move_track = move_tracker
    for n in range(len(move_set)):
        for p in [-1, 1]:
            print 'Current Gamestate: ', game_state
            new_move = attempt_move(deepcopy(game_state.current_setup), move_set[n], deepcopy(game_state.elevator_pos), int(game_state.elevator_pos) + p, deepcopy(game_state.moves_made), move_tracker)
            move_track = new_move[1]
        if new_move[0] != False:
            game_state.add_move(new_move[0])
            if validate_solutions(new_move[0].current_setup) == True:
                print new_move[0].moves_made
    if len(game_state.move_options)>0:
        print 'New Node.'
        for r in range(len(game_state.move_options)):
            print 'Options to move from here are', game_state.move_options
            make_moves(game_state.move_options[r], move_tracker)
    else: print game_state.move_options
def attempt_move(gamestate_setup, moving_pieces, elevator_start, elevator_new, moves_made, move_tracker):
    print 'Setup before move being attempted:', gamestate_setup
    print 'Here is what will be moved:', moving_pieces
    print 'The elevator is on floor ', elevator_start
    print 'The elevator will be moved to floor ', elevator_new
    if elevator_new > 3 or elevator_new < 0:
        print 'bad floor'
        return False, move_tracker
    elif validate_move(deepcopy(gamestate_setup[elevator_new]), deepcopy(gamestate_setup[elevator_start]), moving_pieces, elevator_new) == True:
        print 'good floor'
        #move_tracker.append(hash(frozenset())
        new_node = Game_State(gamestate_setup, elevator_new, moves_made + 1)
        if len(''.join(moving_pieces)) > 2:
            new_node.current_setup[elevator_new].extend(moving_pieces)
        else: new_node.current_setup[elevator_new].append(moving_pieces)
        new_node.current_setup[elevator_new].sort()
        new_node.current_setup[elevator_start] = [x for x in new_node.current_setup[elevator_start] if x not in moving_pieces]
        new_node.current_setup[elevator_start].sort()
        #setup_new[elevator_new].append(elevator_new)
        if  hash(''.join(new_node.current_setup[0])+ '_' + ''.join(new_node.current_setup[1]) + '_' +''.join(new_node.current_setup[2])+ '_' +''.join(new_node.current_setup[3]) + ''.join(str(elevator_new))) in move_tracker:
            print "We've already tried this move."
            return False, move_tracker
        else: 
            move_tracker[hash(''.join(new_node.current_setup[0])+ '_' + ''.join(new_node.current_setup[1]) + '_' +''.join(new_node.current_setup[2])+ '_' +''.join(new_node.current_setup[3]) + ''.join(str(elevator_new)))] = 1
            print 'Move added to log.', new_node
            return new_node, move_tracker
    else:
        print 'Move Invalid'  
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
    #if elevator_pos<0 or elevator_pos>3:
        #return False
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
    tupled_setup = []
    # for n in range(len(setup[elevator_pos])):
    #     tupled_setup.append(tuple(setup[elevator_pos][n]))
    # print tupled_setup
    possible_movers = list(itertools.combinations(setup[elevator_pos], 2)) + setup[elevator_pos]
    # possible_movers = list(itertools.chain.from_iterable(possible_movers))
    return possible_movers


def log_move(move_tracker, floor_config):
    move_tracker.append(hash(frozenset(floor_config)))
    return move_tracker

def validate_solutions(setup):
    if len(setup[0]) + len(setup[1]) + len(setup[2]) == 0:
        print '######PUZZZZZLE SOLVED#######'
        return True
    else: return False

if __name__=='__main__':
    main()

##Just general pseudo-code thoughts: We basically want to take each current setup and determine all possible moves from that setup. We then want to check that move against 
##a hash table to make sure we haven't tried making it before, then we can make a new branch of the tree containing all possible moves from that point. Then we can return the amount of moves it took to get there to find the min.