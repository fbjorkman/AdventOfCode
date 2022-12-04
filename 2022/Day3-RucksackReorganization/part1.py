def convertCharToPrio(char):
	charAsInt = ord(char)
	if charAsInt > 96:
		return charAsInt - 96
	else:
		return charAsInt - 38

def getSameCharPrioValue(firstHalf, secondHalf):
	for char in firstHalf:
		if char in secondHalf:
			return convertCharToPrio(char)

def main():
	prioSum = 0

	with open('input.txt') as data:
		for line in data:
			strippedLine = line.strip()
			half = int(len(strippedLine)/2)
			firstHalf = strippedLine[half:]
			secondHalf = strippedLine[:half]
			prioSum += getSameCharPrioValue(firstHalf, secondHalf)

	print(prioSum)

main()