##AoC_2016_07.py
def check(string):
    for i in range(len(string)-3):
        if string[i] == string[i+3] and string[i+1] == string[i+2] and string[i]!=string[i+1]:
            return True
    return False

def main():
    counter = 0
    for line in open('/Users/jonathanshales/Documents/Programming/Advent/Day_7/data.txt', 'r'):
        trigger = False
        found = False
        if line[0] == '[':
            starter = False
        else: starter = True
        data = line.replace(']','[')
        data = data.split('[')
        for p in data:
            if trigger == True:
                break
            if check(p) == True and starter==True:
                if found == False: 
                    found = True
            elif check(p) ==True and starter==False:
                trigger = True
            if starter ==True:
                starter =False
            else: starter =True
        if found == True and trigger == False:
            counter+=1
    print counter        
if __name__ == "__main__":
    main()