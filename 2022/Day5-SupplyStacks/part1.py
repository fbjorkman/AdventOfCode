import re

def initializeSupplyStacks(firstLine):
	for element in firstLine:
		strippedElement = element.replace(' ','').replace('[','').replace(']','')
		if len(strippedElement) != 0:
			supplyStacks.append([strippedElement])
		else:
			supplyStacks.append([])

def addSupplies(line):
	elements = re.findall('....?', line)
	for i, element in enumerate(elements):
		strippedElement = element.replace(' ','').replace('[','').replace(']','')
		if len(strippedElement) != 0:
			supplyStacks[i].append(strippedElement)


def main():
	result = ''

	with open('input.txt') as data:
		rawFirstLine = data.readline()
		firstLine = re.findall('....?', rawFirstLine)
		initializeSupplyStacks(firstLine)

		for line in data:
			if line.strip().split(' ')[0] == '1':
				break
			addSupplies(line)

		for supplyStack in supplyStacks:
			supplyStack.reverse()

		data.readline()
		for line in data:
			line = line.strip().split(' ')
			amount = int(line[1])
			fromStack = int(line[3])-1
			toStack = int(line[5])-1
			
			for i in range(amount):
				element = supplyStacks[fromStack].pop()
				supplyStacks[toStack].append(element)

		for supplyStack in supplyStacks:
			result += supplyStack.pop()

		print(result)

		
supplyStacks = []
main()