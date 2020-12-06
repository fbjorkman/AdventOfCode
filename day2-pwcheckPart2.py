import re

def main():
	f = open("day2input.txt")
	content = f.readlines()
	number_of_correct_pw = 0

	for line in content:
		list = re.split('-| |:|\n', line)
		p1 = int(list[0])-1
		p2 = int(list[1])-1
		letter = list[2]
		if((list[4][p1] == letter and list[4][p2] != letter) or (list[4][p1] != letter and list[4][p2] == letter)):
			number_of_correct_pw += 1
	print(number_of_correct_pw)

main()