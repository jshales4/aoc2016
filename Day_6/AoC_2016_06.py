##AoC_2016_06.py
def main():
	dict_matrix = [{} for k in range(8)]
	for line in open('/Users/jonathanshales/Documents/Programming/Advent/AOC_16_6.csv', 'r'):
		for q in range(8):
				if line[q] in dict_matrix[q]:
					 dict_matrix[q][line[q]]+=1
				else: dict_matrix[q][line[q]] = 1
	print dict_matrix[0]
	for i in range(8):
		print sorted(dict_matrix[i], key = dict_matrix[i].get)[0]#, reverse=True)[0]##Reverse=True for part 1, omit for part 22
main()