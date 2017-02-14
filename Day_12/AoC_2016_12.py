##AoC_2016_12.py
def main():
    instructions = []
    pos = 0
    print int('1')
    dicto = {'a':0, 'b':0, 'c':1, 'd':0}
    for line in open('/Users/jonathanshales/Documents/Programming/Advent/Day_12/input.txt', 'r'):
        instructions.append(line.rstrip())
    while(len(instructions)>pos):
        result = eval_command(instructions[pos], dicto)
        pos = pos + result[0]
        dicto = result[1]
    print dicto



def eval_command(command, dictionary):
    command = command.split(' ')
    if command[0] == 'cpy':
        try:
            dictionary[command[2]] = int(command[1])
        except ValueError:
            dictionary[command[2]] = dictionary[command[1]]
        return 1, dictionary
    elif command[0] == 'inc':
        dictionary[command[1]] = dictionary[command[1]] + 1
        return 1, dictionary
    elif command[0] == 'dec':
        dictionary[command[1]] = dictionary[command[1]] - 1
        return 1, dictionary
    elif command[0] == 'jnz':
        try:
            if int(command[1]) != 0:
                if int(command[2])<0:
                    return int(command[2]) + 1, dictionary
                else:
                    return int(command[2]), dictionary
        except ValueError:
            if dictionary[command[1]] != 0:
                return int(command[2]), dictionary
            else: return 1, dictionary
    else: print 'Error'

    



if __name__ == '__main__':
    main()