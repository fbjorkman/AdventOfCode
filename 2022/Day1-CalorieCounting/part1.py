def main():
	data = open('input.txt')
	tempsum = 0
	maxsum = 0
	count = 0


	for line in data:
		if line == "\n":
			if maxsum < tempsum:
				maxsum = tempsum
			tempsum = 0
		else:
			tempsum += int(line)
	print(maxsum)


main()