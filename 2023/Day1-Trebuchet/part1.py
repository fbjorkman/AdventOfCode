import re

def __main__():
	with open('input.txt') as data:
		_sum = 0

		for line in data:
			digits = re.findall('\\d', line)
			_sum += int(digits[0] + digits[len(digits)-1])
		print(_sum)

__main__()