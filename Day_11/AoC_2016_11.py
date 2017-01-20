##AoC_2016_11.py
import itertools
def main():
    data = []
    floors = [[1,2,3,4,5], ['x','y','z','a']]
    #Example case
    #floors = [['HM', 'LM'], ['HG'], ['LG'], []]
    #My data
    #floors = [['GST', 'MST', 'GPL', 'MPL'], ['GTH','GRU','MRU','GCU','MCU'],['MTH'],[]]
    elevator = 0
    decide_movers(floors, 0)
    

def decide_movers(setup, elevator_pos):
    possible_movers = []
    possible_movers = list(itertools.combinations(setup[elevator_pos], 2)) + setup[elevator_pos]
    return possible_movers

def attempt_move(setup, moving_pieces, elevator_start, elevator_new):
    proposed_floor = setup + moving_pieces
    if validate_move(setup+moving_pieces, elevator_new) == True:

def log_move(move_tracker, floor_config):
    move_tracker.append(floor_config.sort())
    return move_tracker

def validate_solutions(setup):
    if len(setup[0]) + len(setup[1]) + len(setup[2]) == 0:
        return True
    else: return False

if __name__=='__main__':
    main()

##Just general pseudo-code thoughts: We basically want to take each current setup and determine all possible moves from that setup. We then want to check that move against 
##a hash table to make sure we haven't tried making it before, then we can make a new branch of the tree containing all possible moves from that point. Then we can return the amount of moves it took to get there to find the min.