def numOfNeighbors(i, j):
	count = 0
	
	tempi = i-1
	while tempi >= 0:
		if map[tempi][j] == '#':
			count += 1
			break
		elif map[tempi][j] == 'L':
			break
		tempi -= 1

	tempi = i-1
	tempj = j-1
	while tempi >= 0 and tempj >= 0:
		if map[tempi][tempj] == '#':
			count += 1
			break
		elif map[tempi][tempj] == 'L':
			break
		tempi -= 1
		tempj -= 1

	tempi = i-1
	tempj = j+1
	while tempi >= 0 and tempj < len(map[i]):
		if map[tempi][tempj] == '#':
			count += 1
			break
		elif map[tempi][tempj] == 'L':
			break
		tempi -= 1
		tempj += 1

	tempi = i+1
	while tempi < len(map):
		if map[tempi][j] == '#':
			count += 1
			break
		elif map[tempi][j] == 'L':
			break
		tempi += 1

	tempi = i+1
	tempj = j-1
	while tempi < len(map) and tempj >= 0:
		if map[tempi][tempj] == '#':
			count += 1
			break
		elif map[tempi][tempj] == 'L':
			break
		tempi += 1
		tempj -= 1

	tempi = i+1
	tempj = j+1
	while tempi < len(map) and tempj < len(map[i]):
		if map[tempi][tempj] == '#':
			count += 1
			break
		elif map[tempi][tempj] == 'L':
			break
		tempi += 1
		tempj += 1

	tempj = j-1
	while tempj >= 0:
		if map[i][tempj] == '#':
			count += 1
			break
		elif map[i][tempj] == 'L':
			break
		tempj -= 1

	tempj = j+1
	while tempj < len(map[i]):
		if map[i][tempj] == '#':
			count += 1
			break
		elif map[i][tempj] == 'L':
			break
		tempj += 1

	return count

	
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
					if numOfNeighbors(i, j) == 0:
						change_list.append((i, j))
						changes_made = True
				elif map[i][j] == '#':
					if numOfNeighbors(i, j) >= 5:
						change_list.append((i, j))
						changes_made = True
		for e in change_list:
			if map[e[0]][e[1]] == 'L':
				map[e[0]][e[1]] = '#'
				count += 1
			elif map[e[0]][e[1]] == '#':
				map[e[0]][e[1]] = 'L'
				count -= 1

	print(count)
	

map = []
main()
