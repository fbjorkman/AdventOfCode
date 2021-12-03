def mostCommonBit(num_list, i):
	sumbit = 0
	for number in num_list:
		sumbit += int(number[i])
	if sumbit >= len(num_list)/2:
		return '1'
	else:
		return '0'

def leastCommonBit(num_list, i):
	sumbit = 0
	for number in num_list:
		sumbit += int(number[i])
	if sumbit < len(num_list)/2:
		return '1'
	else:
		return '0'

def filterList(num_filter, num_list):
	matched = []
	for number in num_list:
		if num_filter == number[0:len(num_filter)]:
			matched.append(number)
	return matched

def fromBin(text):
	number = 0
	for i in range(len(text)):
		number += int(text[len(text)-1-i]) * 2**i
	return number

def main():
	rawdata = open('day3data.txt')
	data = rawdata.readlines()
	oxygen_str = ''
	co2_str = ''
	matched = data
	num_filter = ''

	for i in range(len(data[0])):
		mcb = mostCommonBit(matched, i)
		num_filter += mcb
		matched = filterList(num_filter, matched)
		if len(matched) == 1:
			oxygen_str = matched[0].replace('\n','')
			break

	matched = data
	num_filter = ''
	for i in range(len(data[0])):
		lcb = leastCommonBit(matched, i)
		num_filter += lcb
		matched = filterList(num_filter, matched)
		if len(matched) == 1:
			co2_str = matched[0].replace('\n','')
			break
	
	print(fromBin(oxygen_str)*fromBin(co2_str))

main()