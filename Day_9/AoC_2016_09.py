##AoC_2016_09.py
def decompress(string, n, lister):
    for x in range(n):
        lister.append(string)
    return lister
def main():
    uncompressed = []
    pos = 0
    counter = 0
    for word in open('/Users/jonathanshales/Documents/Programming/Advent/Day_9/input.txt', 'r'):
        for c in range(len(word)):
            if pos > 0:
                pos -= 1
                continue
            elif word[c] == '(':
                pos = word[c:].index(')')
                movement = word[c+1:c+pos]
                movement = movement.split('x')
                decompress(word[c+pos+1:c+pos+1+int(movement[0])], int(movement[1]), uncompressed)
                pos += int(movement[0])
            elif word[c] == '\n':
                continue
            else: uncompressed.append(word[c])
    for i in range(len(uncompressed)):
        counter+=len(uncompressed[i])
    print counter
    print uncompressed
if __name__ == "__main__":
    main()