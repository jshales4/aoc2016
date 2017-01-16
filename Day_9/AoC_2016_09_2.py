##AoC_2016_09_2.py

def decompressed_size(file):
    pos = file.find('(')
    end = file.find(')')
    if pos==-1:
        return len(file)
    else:
        movement = file[pos+1:end].split('x')
        for p in range(len(movement)):
            movement[p] = int(movement[p])
        
    return len(file[:pos])+ decompressed_size(file[end+1:movement[0]+end+1]) * movement[1] + decompressed_size(file[movement[0]+end+1:])
def main():
    with open('/Users/jonathanshales/Documents/Programming/Advent/Day_9/input.txt', 'r') as f:
        read_data = f.read()
        total_bytes = decompressed_size(read_data)
    print total_bytes -1 ## For the new line





# def decompressed_size(file, n):
#     counter = 0
#     if file[0] == '(':
#         pos = file[0:].index(')')
#         movement = file[1:pos]
#         movement = movement.split('x')
#         counter = decompressed_size(decompress(file[pos+1:pos+1+int(movement[0])], int(movement[1])) + file[pos+1+int(movement[0]):], n)
#     ##elif file[0] == '\n':
#         ##return n
#     else:
#         try:
#             skipper = file[0:].index('(') 
#             counter =  decompressed_size(file[skipper:], n+skipper)
#         except ValueError:
#             ##print file
#             counter= n + len(file)-2
#     return counter
# def decompress(string, n):
#     lister =''
#     if string.find('(') != -1:
#         for x in range(n):
#             lister = lister + string
#             return lister
# def main():
#     pos = 0
#     with open('/Users/jonathanshales/Documents/Programming/Advent/Day_9/input_test.txt', 'r') as f:
#         read_data = f.read()
#         print read_data
#         total_bytes = decompressed_size(read_data, 0)
#     print total_bytes

if __name__ == "__main__":
    main()