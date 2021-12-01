from collections import deque

def main():
	data = open('day1data.txt')
	prev = float('inf')
	count_increase = 0
	q = deque()
	count = 0

	for line in data:
		q.append(int(line))
		if(len(q) == 4):
			sum1 = q[0]+q[1]+q[2]
			sum2 = q[1]+q[2]+q[3]
			if sum2 > sum1:
				count_increase += 1			
			q.popleft()

	print(count_increase)

main()