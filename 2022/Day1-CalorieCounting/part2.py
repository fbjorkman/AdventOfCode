def main():
	data = open('input.txt')
	tempsum = 0
	maxsums = []


	for line in data:
		if line == "\n":
			if len(maxsums) < 3:
				maxsums.append(tempsum)
				maxsums.sort()
			else:
				if tempsum > maxsums[0]:
					maxsums.pop(0)
					maxsums.append(tempsum)
					maxsums.sort()
			tempsum = 0
		else:
			tempsum += int(line)
	print(sum(maxsums))


main()