def main():
	depth = 0
	horizontal = 0
	data = open('day2data.txt')
	for line in data:
		if line[0] == 'f':
			horizontal += int(line[8])
		elif line[0] == 'u':				
			depth -= int(line[3])
		elif line[0] == 'd':
			depth += int(line[5])
	print(depth*horizontal)

main()