
def split(line):
	return [char for char in line]

def main():
	map = []
	tree_counter1 = 0
	tree_counter2 = 0
	tree_counter3 = 0
	tree_counter4 = 0
	tree_counter5 = 0

	f = open("day3input.txt")
	content = f.readlines()
	for line in content:
		map.append(split(line))

	col_length = len(map[0])-1	# /n char as last char in list
	row_length = len(map)

	#slope 1
	i = 0	#row
	j = 0	#column
	while i < row_length:
		if(map[i][j] == '#'):
			tree_counter1 += 1
		i += 1
		j = (j+1) % col_length
	
	#slope 2
	i = 0	#row
	j = 0	#column
	while i < row_length:
		if(map[i][j] == '#'):
			tree_counter2 += 1
		i += 1
		j = (j+3) % col_length

	#slope 3
	i = 0	#row
	j = 0	#column
	while i < row_length:
		if(map[i][j] == '#'):
			tree_counter3 += 1
		i += 1
		j = (j+5) % col_length

	#slope 4
	i = 0	#row
	j = 0	#column
	while i < row_length:
		if(map[i][j] == '#'):
			tree_counter4 += 1
		i += 1
		j = (j+7) % col_length

	#slope 5
	i = 0	#row
	j = 0	#column
	while i < row_length:
		if(map[i][j] == '#'):
			tree_counter5 += 1
		i += 2
		j = (j+1) % col_length

	print("First slope: ", tree_counter1)
	print("Second slope: ", tree_counter2)
	print("Third slope: ", tree_counter3)
	print("Forth slope: ", tree_counter4)
	print("Fifth slope: ", tree_counter5)
	print("Product: ", tree_counter1*tree_counter2*tree_counter3*tree_counter4*tree_counter5)


main()