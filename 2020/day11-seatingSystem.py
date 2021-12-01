def checkNeighbors(i, j):
	neighbours = []
	checklist = [(i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)]
	if i == 0:
		if (i-1, j-1) in checklist:
			checklist.remove((i-1, j-1))
		if (i-1, j) in checklist:
			checklist.remove((i-1, j))
		if (i-1, j+1) in checklist:
			checklist.remove((i-1, j+1))
	if i == len(map)-1:
		if (i+1, j-1) in checklist:
			checklist.remove((i+1, j-1))
		if (i+1, j) in checklist:
			checklist.remove((i+1, j))
		if (i+1, j+1) in checklist:
			checklist.remove((i+1, j+1))
	if j == 0:
		if (i-1, j-1) in checklist:
			checklist.remove((i-1, j-1))
		if (i, j-1) in checklist:
			checklist.remove((i, j-1))
		if (i+1, j-1) in checklist:
			checklist.remove((i+1, j-1))
	if j == len(map[i])-1:
		if (i-1, j+1) in checklist:
			checklist.remove((i-1, j+1))
		if (i, j+1) in checklist:
			checklist.remove((i, j+1))
		if (i+1, j+1) in checklist:
			checklist.remove((i+1, j+1))

	for e in checklist:
		neighbours.append(map[e[0]][e[1]])

	return neighbours
	
def main():
	f = open('day11input.txt')
	content = f.readlines()
	for line in content:
		map.append(list(line.replace('\n', '')))

	count = 0
	changes_made = True
	change_list = []

	while changes_made:
		changes_made = False
		change_list.clear()
		for i in range(len(map)):
			for j in range(len(map[i])):
				if map[i][j] == 'L':
					if '#' not in checkNeighbors(i,j):
						change_list.append((i, j))
						changes_made = True
				elif map[i][j] == '#':
					if checkNeighbors(i,j).count('#') >= 4:
						change_list.append((i, j))
						changes_made = True

		for e in change_list:
			if map[e[0]][e[1]] == 'L':
				map[e[0]][e[1]] = '#'
			elif map[e[0]][e[1]] == '#':
				map[e[0]][e[1]] = 'L'
	

	for i in range(len(map)):
		count += map[i].count('#')
	print(count)
	

map = []
main()
