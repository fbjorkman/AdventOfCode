import itertools
import re

def recursiveCheck(bag):
	if noBagRegex.match(bag):
		return 0
	else:
		connected_bags = str(kvstore.get(bag)).split(', ')
		bagcount = 0
		for newbag in connected_bags:
			if noBagRegex.match(newbag):
				continue
			if newbag[0] == '1':
				nextbag = newbag[2:] + 's'
			else:
				nextbag = newbag[2:]

			bagcount += int(newbag[0]) + int(newbag[0])*recursiveCheck(nextbag)

		return bagcount


def main():
	f = open('day7input.txt')
	content = f.readlines()
	count = 0

	for line in content:
		temp = line.split(' contain ')
		kvstore[temp[0]] = temp[1].replace('\n', '').replace('.', '')
	
	print(recursiveCheck('shiny gold bags'))

noBagRegex = re.compile('no other bags')
kvstore = dict()
approvedbags = dict()
disapprovedbags = dict()
main()