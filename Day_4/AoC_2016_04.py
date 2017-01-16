# ##AoC_2016_03.py


def main():
	good_ids_sum = 0 #Part 1 stuff
	file = open("AOC_4_Solution.txt", "w")
	for line in open('/Users/jonathanshales/Documents/Programming/Advent/AOC_16_4.csv', 'r'):
		dictionary = {}
		lister=[]
		data = line.split('-')
		for n in data:
			if n[0].isdigit():
				number = n[0:3]
				common_chars = n[4:9]
			else: 
				for q in range(len(n)):
					if n[q] in dictionary:
						dictionary[n[q]] +=1
					else: dictionary[n[q]] = 1
		lister = [(j, k) for k, j in dictionary.iteritems()]
		lister = sorted(lister, key=lambda x: x[1])
		lister = sorted(lister, key=lambda x: x[0], reverse = True)
		## could try lister = sorted(lister, key=lambda x:-x[0], x[1])
		lister = lister[0:5]
		lister = [x[1] for x in lister]
		

	# 	if sorted(lister)==sorted(common_chars):
	# 		good_ids_sum=good_ids_sum+int(number)
	# print good_ids_sum # This is part 1 only

		if sorted(lister)==sorted(common_chars):
			for a in line:
				if a == "-":
					file.write(' ')
				elif ord(a) + (int(number) % 26) > 122:
					file.write(chr(ord(a) + (int(number) % 26 - 26)))
				elif ord(a)<97:
					file.write(" %d\n" % (int(number)))
					break
				elif ord(a) + int(number) % 26 <123:
					file.write(chr(ord(a) + int(number) % 26))
				else:
					file.write("$")#for error checking 
	file.close()



main()