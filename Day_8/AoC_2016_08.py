##AoC_2016_08.py
def add_squares(addthem, grid):
    square_gen = addthem.split('x')
    for i in range(int(square_gen[1])):
        for j in range(int(square_gen[0])):
            if grid[i][j] == '.':
                grid[i][j] = '#'
    return grid

def shift(moveright, grid):
    move = moveright.split(' by ')
    for n in range(len(move)):
        move[n] = int(move[n])
    new_row = grid[move[0]][len(grid[move[0]])-move[1]:] + grid[move[0]][:len(grid[move[0]])-move[1]]
    for i in range(len(grid[move[0]])):
        grid[move[0]][i]=new_row[i]
    return grid

    
def main():
    matrix=[['.' for x in range(50)]for y in range(6)]
    counter = 0
    for line in open('/Users/jonathanshales/Documents/Programming/Advent/Day_8/input.txt', 'r'):
        if line[0:4] == "rect":
            command = line[5:]
            matrix = add_squares(command, matrix)
        elif line[7:10] =='col':
            matrix = shift(line[16:], [list(a) for a in zip(*matrix)])
            matrix = [list(a) for a in zip(*matrix)]
        elif line[7:10]=='row':
            matrix = shift(line[13:], matrix)    
    for n in range(6):
        for m in range(50):
            if matrix[n][m] == '#':
                print matrix[n][m],
                counter+=1
            else: print ' ',
        print '\n'
    print 'The total number of #s is ', counter
if __name__ == "__main__":
    main()