def main():
	data = open('day1data.txt')
	prev = float('inf')
	count_increase = 0

	for line in data:
		if int(line) > prev:
			count_increase += 1
		prev = int(line)

	print(count_increase)

main()