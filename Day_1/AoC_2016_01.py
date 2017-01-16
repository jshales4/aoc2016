##AoC_2016_01.py test
def main():
	data = []
	instructions =open('/Users/jonathanshales/Documents/Programming/Advent/AOC_16_1_1.csv', 'r')
	data = instructions.read().split(',')
	x = 0
	y = 0
	direction = 1
	loc_log = {}
	for i in range(len(data)):
		data[i]=data[i].strip()
		distance = int(data[i][1:])
		if data[i][0] == 'L':
			direction = direction - 1
		elif data[i][0] == 'R':
			direction = direction + 1
		if direction>4:
			direction = 1
		elif direction<1:
				direction = 4
		for p in range(distance):
			if direction == 1: 
				y = y + 1
			elif direction == 2:
				x = x + 1
			elif direction == 3: 
				y = y - 1
			elif direction ==4:
				x = x - 1		
			location = hash(str((x,y)))
			if location in loc_log:
				print "We have visited (",x,",",y,") more than once, and it is ",abs(x)+abs(y)," blocks away from the origin"
			loc_log.update({location:x+y})
		
	print "The instructions end at a point ", abs(x) + abs(y), "blocks away from the origin."
main()



