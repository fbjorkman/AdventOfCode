from collections import deque
import itertools

def getMin():
	min = queue[0]
	for e in queue:
		if e < min:
			min = e
	return min

def getMax():
	max = queue[0]
	for e in queue:
		if e > max:
			max = e
	return max

def main():
	f = open('day9input.txt')
	content = f.readlines()
	totSum = 0
	for a in content:
		totSum += int(a)
		queue.append(int(a))
		if totSum == answer_from_part1:
			print('min: ', getMin(), 'max: ', getMax(), 'SumMinMax: ', getMin()+getMax())
			return
		elif totSum > answer_from_part1:
			totSum -= queue.popleft()
			while totSum >= answer_from_part1:
				if totSum == answer_from_part1:
					print('min: ', getMin(), 'max: ', getMax(), 'SumMinMax: ', getMin()+getMax())
					return
				totSum -= queue.popleft()

answer_from_part1 = 21806024
queue = deque()
main()