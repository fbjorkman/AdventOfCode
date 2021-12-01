def main():
	f = open('day10input.txt')
	content = f.readlines()
	sortedArr = []
	for line in content:
		sortedArr.append(int(line))
	sortedArr.sort()
	count1 = 0
	count3 = 0
	for i in range(len(sortedArr)-1):
		diff = sortedArr[i+1] - sortedArr[i]
		if diff == 1:
			count1 += 1
		elif diff == 3:
			count3 += 1
	count1 += 1	#start
	count3 += 1	#stop
	print(len(sortedArr))
	print(count1, count3, count1*count3)

main()