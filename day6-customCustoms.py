def main():
	f = open('day6input.txt')
	content = f.readlines()
	totSum = 0
	ans = set()
	for line in content:
		if line == '\n':
			totSum += len(ans)
			ans.clear()
			continue
		for c in line.replace('\n', ''):
			ans.add(c)
	totSum += len(ans)
	print(totSum)

main()