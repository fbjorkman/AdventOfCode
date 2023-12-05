def __main__():

	with open('input.txt') as data:
		power_sum = 0

		for line in data:
			color_map = {'red': 0, 'green': 0, 'blue': 0}
			game_info = line.strip().split(': ')
			sets = game_info[1].split(';')
			for _set in sets:
				_set = _set.strip().replace(',', '').split(' ')
				update_min_set_elements(_set, color_map)
			power_sum += color_map['red'] * color_map['green'] * color_map['blue']

	print(power_sum)

def update_min_set_elements(_set, color_map):
	for i in range(0, len(_set), 2):
		if color_map[_set[i+1]] < int(_set[i]):
			color_map[_set[i+1]] = int(_set[i])

__main__()