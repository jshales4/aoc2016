##AoC_2016_03.py
def main():
	good_triangles = 0
	bad_triangles = 0
	for line in open('/Users/jonathanshales/Documents/Programming/Advent/AOC_16_3_adj.csv', 'r'):
		data = line.split()
		data = list(map(int, data))
		data.sort()
		if data[0] + data[1] > data[2]:
			good_triangles+=1
		else: bad_triangles+=1
	print "There are ", good_triangles, "good triangles and ", bad_triangles, "bad triangles"
main()

# def main():
# 	good_triangles = 0
# 	bad_triangles = 0
# 	counter= 0
# 	f= open('/Users/jonathanshales/Documents/Programming/Advent/AOC_16_3_adj.csv', 'w+')
# 	for i in range(3):
# 		for line in open('/Users/jonathanshales/Documents/Programming/Advent/AOC_16_3.csv', 'r'):
# 			data=line.split()
# 			f.write(data[i])
# 			f.write("\t")
# 			counter+=1
# 			if counter ==3:
# 				f.write("\n")
# 				counter = 0
# 	f.close()
# main()
