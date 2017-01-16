##AoC_2016_10_2.py
def give_chips(giver_bot, bot_tracker):
    bot_tracker[bot_tracker[giver_bot].gives_high_to].get_chip(bot_tracker[giver_bot].high_chip)
    bot_tracker[bot_tracker[giver_bot].gives_low_to].get_chip(bot_tracker[giver_bot].low_chip)
    bot_tracker[giver_bot].remove_chips(bot_tracker[giver_bot].high_chip, bot_tracker[giver_bot].low_chip )
    return bot_tracker


class bot:
    def __init__ (self, bot_num):
        self.botnumber = bot_num
        self.gives_high_to = 0
        self.gives_low_to = 0
        self.low_chip = 0
        self.high_chip = 0
        self.chips = []

    def update_rules(self, gives_low, gives_high):
        if gives_high != 'n':
            self.gives_high_to = gives_high
        if gives_low != 'n':
            self.gives_low_to = gives_low

    def get_chip(self, chip_num):
        chips_ordered = []
        self.chips.append(chip_num)
        if len(self.chips) > 1:
            if self.chips[0]<self.chips[1]:
                self.low_chip = self.chips[0]
                self.high_chip = self.chips[1]
            else: 
                self.low_chip = self.chips[1]
                self.high_chip = self.chips[0]

    def evaluate_bot(self):
        if len(self.chips)>1:
            return True
        else: return False

    def remove_chips(self, chip1, chip2):
        self.chips.remove(chip1)
        self.chips.remove(chip2)

    def report_inventory(self):
        return self.high_chip, self.low_chip

def main():
    bot_tracker = {}
    for line in open('/Users/jonathanshales/Documents/Programming/Advent/Day_10/input.txt', 'r'):
        command = line.split(' ')
        if command[0] == 'value':
            if int(command[5]) not in bot_tracker:
                bot_tracker[int(command[5])] = bot(int(command[5]))
            bot_tracker[int(command[5])].get_chip(int(command[1]))
        elif command[0] == 'bot':
            if int(command[1]) not in bot_tracker:
                bot_tracker[int(command[1])] = bot(int(command[1])) 
            if command[5] == 'output':
                if -1*int(command[6]) not in bot_tracker:
                    bot_tracker[-1*int(command[6])] = bot(-1*int(command[6]))
                    bot_tracker[int(command[1])].update_rules(-1*int(command[6]),'n')
            else: 
                if int(command[6]) not in bot_tracker:
                    bot_tracker[int(command[6])] = bot(int(command[6]))
                bot_tracker[int(command[1])].update_rules(int(command[6]),'n')

            if len(command)>7 and  command[10]=='output':
                if -1*int(command[11]) not in bot_tracker:
                    bot_tracker[-1*int(command[11])] = bot(-1*int(command[11]))
                bot_tracker[int(command[1])].update_rules('n',-1*int(command[11]))
            elif len(command)>7:
                if int(command[11]) not in bot_tracker:
                    bot_tracker[int(command[11])] = bot(int(command[11]))
                bot_tracker[int(command[1])].update_rules('n',int(command[11]))
    
    keep_going = True
    while keep_going:
        keep_going = False
        for i in bot_tracker:
            if bot_tracker[i].botnumber < 0:
                continue
            else:
                if bot_tracker[i].evaluate_bot()==True:
                    bot_tracker = give_chips(i, bot_tracker)
                    keep_going = True
    for n in bot_tracker:## Part 1 Answer
        if bot_tracker[n].low_chip == 17 and bot_tracker[n].high_chip == 61:
            print bot_tracker[n].botnumber, 'has the task of comparing chips 61 and 17'       
   
    product = [] ##Part2 Answer
    for x in [-1000,-1,-2]:
        product.append(bot_tracker[x].chips)
    print int(product[0][0]) * int(product[1][0]) * int(product[2][0]), 'is the product of those three outputs'

if __name__=="__main__":
    main()

