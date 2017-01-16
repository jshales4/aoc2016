##AoC_2016_02.py
numpad = {1:1, 2:2, 3:3, 11:4, 12:5, 13:6, 21:7, 22:8, 23:9}##This is the numpad for part 1
numpad2= {3:1, 12:2, 13:3, 14:4, 21:5, 22:6, 23:7, 24:8, 25:9, 32:"A", 33:"B", 34:"C", 43:"D"}#This is the numpad for part 2
def evaluate_button(newlocation, oldlocation):
	if newlocation in numpad2:
		return newlocation
	else: 
		return oldlocation

def main():
	data = []
	button = 21
	proposed = 0
	for line in open('/Users/jonathanshales/Documents/Programming/Advent/AOC_16_2.csv', 'r'):
		for c in line:
			if c == "U":
				proposed = button - 10
			elif c == "D":
				proposed = button + 10
			elif c == "L": 
				proposed = button -1
			elif c == "R":
				proposed = button + 1
			button = evaluate_button(proposed,button)
		data.append(numpad2[button])
	print(data)

main()