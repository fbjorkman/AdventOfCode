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

		data.readline()
		for line in data:
			line = line.strip().split(' ')
			amount = int(line[1])
			fromStack = int(line[3])-1
			toStack = int(line[5])-1
			supplyStacks[toStack] = supplyStacks[fromStack][:amount] + supplyStacks[toStack]
			supplyStacks[fromStack] = supplyStacks[fromStack][amount:]

		for supplyStack in supplyStacks:
			result += supplyStack[0]

		print(result)

		
supplyStacks = []
main()