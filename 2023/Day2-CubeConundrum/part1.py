def __main__():

	with open('input.txt') as data:
		id_sum = 0

		for line in data:
			elements = line.replace(':', '').replace(';', '').replace(',', '').strip().split(' ')
			game_id = int(elements[1])
			if not impossible_game(elements[2:]):
				id_sum += game_id

	print(id_sum)

def impossible_game(elements):
	color_map = {'red': 12, 'green': 13, 'blue': 14}
	for i in range(0, len(elements), 2):
		if color_map[elements[i+1]] < int(elements[i]):
			return True
	return False

__main__()