def checkCompletlyOverlappedRanges(rangeA, rangeB):
	aMin = int(rangeA[0])
	aMax = int(rangeA[1])
	bMin = int(rangeB[0])
	bMax = int(rangeB[1])
	return aMin <= bMin and aMax >= bMax or aMin >= bMin and aMax <= bMax

def main():
	count = 0

	with open('input.txt') as data:
		for line in data:
			ranges = line.strip().split(',')
			firstRange = ranges[0].split('-')
			secondRange = ranges[1].split('-')
			if checkCompletlyOverlappedRanges(firstRange, secondRange):
				count += 1

	print(count)


main()