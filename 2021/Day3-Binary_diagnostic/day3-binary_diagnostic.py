def main():
	data = open('day3data.txt')
	data = data.readlines()
	sumarr = [0 for i in range(len(data[0])-1)]
	gamma = 0
	epsilon = 0
	for line in data:
		line_arr = list(line.replace('\n',''))
		for i in range(len(line_arr)):
			sumarr[i] += int(line_arr[i])
	for i in range(len(sumarr)):
		if sumarr[len(sumarr)-1-i] > len(data)/2:
			gamma += 2**i
		else:
			epsilon += 2**i
	print(gamma*epsilon)



main()