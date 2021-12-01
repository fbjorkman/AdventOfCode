def subCombinations(list, offset):
	print(list)
	if len(list)-offset < 2:
		return 1
	elif len(list)-offset == 2:
		return 2
	elif len(list)-offset == 3:
		return 4
	elif len(list)-offset == 4:
		return 7

def main():
	f = open('day10input.txt')
	content = f.readlines()
	sortedArr = []
	for line in content:
		sortedArr.append(int(line))
	sortedArr.sort()
	multlist = []
	templist = []
	templist.append(1)	#first step (from outlet to first adapter)
	for i in range(1, len(sortedArr)):
		diff = sortedArr[i] - sortedArr[i-1]
		if diff == 1:
			templist.append(1)
		elif diff == 3:
			multlist.append(subCombinations(templist, 0))
			templist.clear()
		totalCombinations = 1
	multlist.append(subCombinations(templist, 0))	#last step (from last adapter to build in adapter) ends with 3

	for e in multlist:
		totalCombinations *= e
	print(totalCombinations)


main()
print(subCombinations([1,1,1,1,1,1], 0))