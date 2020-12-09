from collections import deque
import itertools

def checkSum(a):
	for e1 in queue:
		for e2 in itertools.islice(queue, queue.index(e1)+1, None):
			if int(e1) + int(e2) == int(a):
				return True
	return False

def main():
	f = open('day9input.txt')
	content = f.readlines()
	for a in content:
		if len(queue) == 25:
			if not checkSum(a):
				return a
			queue.popleft()
		queue.append(int(a))



queue = deque()
print(main())