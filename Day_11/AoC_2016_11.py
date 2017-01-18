##AoC_2016_11.py
def main():
    data = []
    floors = [['HM', 'LM'], ['HG'], ['LG'], []]
    ##floors = [['GST', 'MST', 'GPL', 'MPL'], ['GTH','GRU','MRU','GCU','MCU'],['MTH'],[]]
    elevator = 0
    # for line in open('/Users/jonathanshales/Documents/Programming/Advent/Day_11/input_test.txt', 'r'):
    #     data = line.split(' a ')
    #     floors.append(data)
    # print floors
    for n in floors:

def decide_movers(setup, elevator_pos):
    possible_movers = []
    for n in range(len(setup[elevator_pos])):
        possible_movers.append(setup[elevator_pos[n]])



def validate_solutions(setup):
    if len(setup[0]) + len(setup[1]) + len(setup[2]) == 0:
        return True
    else: return False

if __name__=='__main__':
    main()

##Just general pseudo-code thoughts: We basically want to take each current setup and determine all possible moves from that setup. We then want to check that move against 
##a hash table to make sure we haven't tried making it before, then we can make a new branch of the tree containing all possible moves from that point. Then we can return the amount of moves it took to get there to find the min.