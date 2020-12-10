def main():
	f = open('day6input.txt')
	content = f.readlines()
	totSum = 0
	ans = set()
	first_line = True
	for line in content:
		if line == '\n':
			totSum += len(ans)
			ans.clear()
			first_line = True
			continue
		if first_line:
			for c in line.replace('\n', ''):
				ans.add(c)
			first_line = False
		else:
			disc_list = []
			for c in ans:
				if c not in line:
					disc_list.append(c)
			for c in disc_list:
				ans.discard(c)
				
	totSum += len(ans)
	print(totSum)

main()