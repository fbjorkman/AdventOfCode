import re

def main():
	f = open("day2input.txt")
	content = f.readlines()
	number_of_correct_pw = 0

	for line in content:
		list = re.split('-| |:|\n', line)
		min = int(list[0])
		max = int(list[1])
		letter = list[2]
		occurance = list[4].count(letter)
		if(occurance >= min and occurance <= max):
			number_of_correct_pw += 1
	print(number_of_correct_pw)

main()