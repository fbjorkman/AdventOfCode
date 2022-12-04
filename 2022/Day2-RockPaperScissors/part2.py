shapes = {'A':1, 'B':2, 'C':3}
result = {'X':0, 'Y':3, 'Z':6}
needLoss = {'A':'C', 'B':'A', 'C':'B'}
needWin = {'A':'B', 'B':'C', 'C':'A'}

def myPick(opponentShape, result):
	if result == 'Y':
		return opponentShape
	if result == 'X':
		return needLoss[opponentShape]
	else:
		return needWin[opponentShape]

def main():
	score = 0

	with open('input.txt') as data:
		for line in data:
			elements = line.strip().split(' ')
			myShape = myPick(elements[0], elements[1])
			score += result[elements[1]] + shapes[myShape]

	print(score)


main()