##AoC_2016_15.py
def main():
    data = []
    command_list = []
    through = False
    drop_time = 0
    for line in open('/Users/jonathanshales/Documents/Programming/Advent/Day_15/input.txt', 'r'):
        commands = []
        data = line.split()
        data[1] = data[1].replace("#","")
        data[11] = data[11].replace(".","")
        commands.append(int(data[1]))
        commands.append(int(data[3]))
        commands.append(int(data[11]))
        commands = tuple(commands)
        command_list.append(commands)
    command_list.append((7,11,0))##For part 2
    

    while through == False:
        through = evaluate_drop(command_list, drop_time, 0)
        drop_time += 1

    print drop_time -1



def evaluate_drop(command_list, drop_time, pos):
    if (command_list[pos][2]+drop_time+command_list[pos][0])%command_list[pos][1] == 0:
        if pos>5:
            return True
        else:
            return evaluate_drop(command_list, drop_time, pos +1)
    else:
        return False

if __name__ == '__main__':
    main()