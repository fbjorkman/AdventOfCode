import re

def __main__():
	with open('input.txt') as data:
		_sum = 0

		for line in data:
			modified_line = _replace_numbers(line)
			digits = re.findall('\\d', modified_line)
			_sum += int(digits[0] + digits[len(digits)-1])
		print(_sum)

def _replace_numbers(line):
	line = re.sub('one', 'one1one', line)
	line = re.sub('two', 'two2', line)
	line = re.sub('three', 'three3three', line)
	line = re.sub('four', 'four4', line)
	line = re.sub('five', 'five5five', line)
	line = re.sub('six', 'six6', line)
	line = re.sub('seven', 'seven7seven', line)
	line = re.sub('eight', 'eight8eight', line)
	return re.sub('nine', 'nine9nine', line)

__main__()