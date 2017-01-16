##AoC_2016_07_2.py
def check(string, aba_list, bab_list, starter):
    for i in range(len(string)-2):
        if string[i] == string[i+2] and string[i]!=string[i+1]:
            if starter == True:
                aba_list.append(string[i:i+3])
            else: 
                bab_list.append(string[i:i+3])

def main():
    counter = 0
    for line in open('/Users/jonathanshales/Documents/Programming/Advent/Day_7/data_copy.txt', 'r'):
        abas = []
        babs = []
        babs_flipped = []
        data = line.replace(']','[')
        data = data.split('[')
        if line[0] == '[':
            starter = False
        else: starter = True
        for p in data:
            check(p, abas, babs, starter)
            if starter ==True:
                starter =False
            else: starter =True
        for n in babs:
            s = n[1]+n[0]+n[1]
            if s in abas:
                counter +=1 
                break
    print counter

if __name__ == "__main__":
    main()



    #     trigger = False
    #     found = False
        

    #     for p in data:
    #         if trigger == True:
    #             break
    #         if check(p) == True and starter==True:
    #             if found == False: 
    #                 found = True
    #         elif check(p) ==True and starter==False:
    #             trigger = True
    #         if starter ==True:
    #             starter =False
    #         else: starter =True
    #     if found == True and trigger == False:
    #         counter+=1
    # print counter        
