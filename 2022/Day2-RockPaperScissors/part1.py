def outcome(opponentShape, myShape):
	if myShape == opponentShape:
		return 3
	if myShape == 'X':
		if opponentShape == 'Z':
			return 6
		else:
			return 0
	if myShape == 'Y':
		if opponentShape == 'X':
			return 6
		else:
			return 0
	if myShape == 'Z':
		if opponentShape == 'Y':
			return 6
		else:
			return 0



def main():
	opponentShapes = {'A':'X', 'B':'Y', 'C':'Z'}
	myShapes = {'X':1, 'Y':2, 'Z':3}
	score = 0

	with open('input.txt') as data:
		for line in data:
			elements = line.strip().split(' ')
			score += myShapes[elements[1]] + outcome(opponentShapes[elements[0]], elements[1])

	print(score)


main()