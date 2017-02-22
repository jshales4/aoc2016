##AoC_2016_13.py
def main():
    #print is_wall(2,2)
    move_tracker = {}
    start=Current_Position(1,1,0)
    solution_finder=0
    dict_size=0
    while solution_finder==0:
        result = climb_tree(start, move_tracker)
        move_tracker = result[0]
        solution_finder = result[1]
    for n in move_tracker:
        if n<51:
            dict_size= dict_size + 1
    print dict_size
        
def is_wall(x, y): ##returns True if a wall and False if a space
    if x < 0 or y < 0:
        return True
    counter =0 
    loc = str(bin(x*x + 3*x + 2*x*y + y + y*y+1362))
    for n in range(len(loc)):
        if loc[n]=='1':
            counter += 1
    if counter%2 == 1:
        return True
    else: return False

def climb_tree(position, move_tracker):
    if len(position.move_options)==0:
        attempt = make_moves(position,move_tracker)
        move_tracker = attempt[0]
        position.moves_remain = False
        if attempt[1]>0:
            return attempt[0], attempt[1]
    else: 
        for n in position.move_options:
            attempt = climb_tree(n,move_tracker)
            move_tracker = attempt[0]
            if attempt[1]>1:
                return move_tracker, attempt[1]
    return move_tracker, 0



def make_moves(position, move_tracker):
    for n in [-1,1]:
            if is_wall(position.xpos, position.ypos+n) == False:
                if check_solutions(position.xpos, position.ypos+n)==True:
                    print position.moves_made+1
                    return move_tracker, position.moves_made + 1
                if hash(str(position.xpos)+ '_' + str(position.ypos+n)) not in move_tracker or move_tracker[hash(str(position.xpos)+ '_' + str(position.ypos+n))]>position.moves_made+1:
                    move_tracker[hash(str(position.xpos)+ '_' + str(position.ypos+n))] = position.moves_made + 1
                    position.add_move(Current_Position(position.xpos, position.ypos+n, position.moves_made + 1))
            if is_wall(position.xpos+n, position.ypos) == False:
                if check_solutions(position.xpos+n, position.ypos)==True:
                    print position.moves_made +1
                    return move_tracker, position.moves_made + 1
                if hash(str(position.xpos+n)+ '_' + str(position.ypos)) not in move_tracker or move_tracker[hash(str(position.xpos+n)+ '_' + str(position.ypos))]>position.moves_made+1:
                    move_tracker[hash(str(position.xpos+n)+ '_' + str(position.ypos))] = position.moves_made + 1
                    position.add_move(Current_Position(position.xpos+n, position.ypos, position.moves_made + 1))
    return move_tracker, 0

def check_solutions(xpos, ypos):
    if xpos == 31 and ypos == 39:
        return True
    else: return False

class Current_Position:
    def __init__(self, xpos, ypos, moves_made):
        self.xpos = xpos
        self.ypos = ypos
        self.moves_made = moves_made
        self.move_options = []
        self.moves_remain = True

    def add_move (self, new_position):
        self.move_options.append(new_position)

if __name__ == '__main__':
    main()