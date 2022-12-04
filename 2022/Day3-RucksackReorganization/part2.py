def convertCharToPrio(char):
	charAsInt = ord(char)
	if charAsInt > 96:
		return charAsInt - 96
	else:
		return charAsInt - 38

def getCommonElements(first, second):
	commonChars = []
	for element in first:
		if element in second:
			commonChars.append(element)
	return commonChars

def getCommonElement(first, second, third):
	for element in first:
		if element in second and element in third:
			return element

def main():
	prioSum = 0

	with open('input.txt') as data:
		batch = []
		for line in data:
			strippedLine = line.strip()
			batch.append(strippedLine)
			if len(batch) == 3:
				commonFirstSecond = getCommonElements(batch[0], batch[1])
				commonFirstThird = getCommonElements(batch[0], batch[2])
				commonSecondThird = getCommonElements(batch[1], batch[2])
				groupBadge = getCommonElement(commonFirstSecond, commonFirstThird, commonSecondThird)
				prioSum += convertCharToPrio(groupBadge)
				batch.clear()

	print(prioSum)

main()