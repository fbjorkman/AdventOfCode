def mySeat(arr):
	for i in range(8):
		if i not in arr:
			return i

def main():
	f = open('day5input.txt')
	content = f.readlines()
	size = len(content)
	passport_check = [[] for i in range(128)]
	for line in content:
		min = 0
		max = 128
		for i in range(6):
			if line[i] == 'F':
				max = (min+max)/2
			else:
				min = (min+max)/2
		if line[6] == 'F':
			index = int(min)
		else:
			index = int(max-1)
		min = 0
		max = 8
		for i in range(2):
			if line[7+i] == 'L':
				max = (min+max)/2
			else:
				min = (min+max)/2
		if line[9] == 'L':
			passport_check[index].append(min)
		else:
			passport_check[index].append(max-1)

	for i in range(128):
		if len(passport_check[i]) == 7:
			seatId = int(i * 8 + mySeat(passport_check[i]))
			print(seatId)
			return



main()