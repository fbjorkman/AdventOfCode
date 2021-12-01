
def split(line):
	return [char for char in line]

def main():
	map = []
	tree_counter = 0
	f = open("day3input.txt")
	content = f.readlines()
	for line in content:
		map.append(split(line))

	col_length = len(map[0])-1	# /n char as last char in list
	row_length = len(map)

	i = 0	#row
	j = 0	#column
	while i < row_length:
		if(map[i][j] == '#'):
			tree_counter += 1
		i += 1
		j = (j+3) % col_length
	print(tree_counter)

main()