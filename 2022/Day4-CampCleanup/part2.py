def checkOverlap(rangeA, rangeB):
	aMin = int(rangeA[0])
	aMax = int(rangeA[1])
	bMin = int(rangeB[0])
	bMax = int(rangeB[1])
	return aMin >= bMin and aMin <= bMax or bMin >= aMin and bMin <= aMax

def main():
	count = 0

	with open('input.txt') as data:
		for line in data:
			ranges = line.strip().split(',')
			firstRange = ranges[0].split('-')
			secondRange = ranges[1].split('-')
			if checkOverlap(firstRange, secondRange):
				count += 1

	print(count)


main()