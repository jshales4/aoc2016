##AoC_2016_11.py
import itertools
def main():
    data = []
    floors = [[1,2,3,4,5], ['x','y','z','a']]
    move_tracker = {}
    #Example case
    floors = [['HM', 'LM'], ['HG'], ['LG'], []]
    #My data
    #floors = [['SG', 'SM', 'PG', 'PM'], ['TG','RG','RM','CG','CM'],['TM'],[]]
    elevator = 0
    #decide_movers(floors, 0)
    attempt_move(floors,'HM', 0, 1, move_tracker)

def make_moves(setup, elevator_pos, move_tracker, move_counter):
    move_set = decide_movers(setup, elevator_pos)
    for n in move_set:
        for p in [-1, 1]:
            if attempt_move(setup, n, elevator_pos, elevator_pos + p, move_tracker) == True:
    

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

def validate_move(proposed_floor, elevator_passengers, elevator_pos):
    if elevator_pos<0 or elevator_pos>3:
        return False
    elif len(''.join(elevator_passengers)) > 2:
        if elevator_passengers[0][1] == 'G' and elevator_passengers[1][1] == 'M' and elevator_passengers[0][0] != elevator_passengers[1][0]:
            return False
        elif elevator_passengers[1][1] == 'G' and elevator_passengers[0][1] == 'M' and elevator_passengers[0][0] != elevator_passengers[1][0]:
            return False
        else:
            proposed_floor.extend(elevator_passengers) 
            return valid_floor(proposed_floor)    
    else: 
        proposed_floor.append(elevator_passengers)
        return valid_floor(proposed_floor)



def decide_movers(setup, elevator_pos):
    possible_movers = []
    possible_movers = list(itertools.combinations(setup[elevator_pos], 2)) + setup[elevator_pos]
    return possible_movers

def attempt_move(setup, moving_pieces, elevator_start, elevator_new, move_tracker):
    setup_new = setup[:]
    if validate_move(setup_new[elevator_new], moving_pieces, elevator_new) == True:
        #move_tracker.append(hash(frozenset())
        setup_new[elevator_new].append(moving_pieces)
        setup_new[elevator_new].sort()
        setup_new[elevator_start] = [x for x in setup[elevator_start] if x not in moving_pieces]
        setup_new[elevator_start].sort()
        setup_new[elevator_new].append(elevator_new)
        print setup_new
        if hash(frozenset(setup_new[0] + setup_new[1] + setup_new[2] + setup_new[3])) in move_tracker:
            return False
        else: return True
    else: return False

def log_move(move_tracker, floor_config):
    move_tracker.append(hash(frozenset(floor_config)))
    return move_tracker

def validate_solutions(setup):
    if len(setup[0]) + len(setup[1]) + len(setup[2]) == 0:
        return True
    else: return False

if __name__=='__main__':
    main()

##Just general pseudo-code thoughts: We basically want to take each current setup and determine all possible moves from that setup. We then want to check that move against 
##a hash table to make sure we haven't tried making it before, then we can make a new branch of the tree containing all possible moves from that point. Then we can return the amount of moves it took to get there to find the min.