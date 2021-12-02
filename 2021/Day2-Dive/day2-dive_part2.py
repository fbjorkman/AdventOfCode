def main():
	depth = 0
	horizontal = 0
	aim = 0
	data = open('day2data.txt')
	for line in data:
		if line[0] == 'f':
			horizontal += int(line[8])
			depth += int(line[8])*aim
		elif line[0] == 'u':				
			aim -= int(line[3])
		elif line[0] == 'd':
			aim += int(line[5])
	print(depth*horizontal)

main()