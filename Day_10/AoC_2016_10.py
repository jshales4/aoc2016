##AoC_2016_10.py

def bot_transaction(giver,receiver,bin_flag, high, command, bot_tracker):
    if bin_flag*int(command[receiver]) not in bot_tracker:
        bot_tracker[bin_flag*int(command[receiver])] = []
    bot_tracker[bin_flag*int(command[receiver])].append(bot_tracker[int(command[giver])].sort().pop(high))
    return bot_tracker
def main():
    bot_tracker = {}
    for line in open('/Users/jonathanshales/Documents/Programming/Advent/Day_10/input.txt', 'r'):
        command = line.split(' ')
        if command[0] == 'value':
            if int(command[5]) not in bot_tracker:
                bot_tracker[int(command[5])] = []
            bot_tracker[int(command[5])].append(int(command[1]))
        elif command[0] == 'bot':
            if command[5] == 'output':
                bot_tracker = bot_transaction(1,6,-1,0, command, bot_tracker)
            else: bot_tracker = bot_transaction(1,6,1,0, command, bot_tracker)
            if len(command)>7 and  command[10]=='output':
                bot_tracker = bot_transaction(1,11,-1,1, command, bot_tracker)
            elif len(command)>7:
                bot_tracker = bot_transaction(1,11,1,1, command, bot_tracker)
   


if __name__=="__main__":
    main()