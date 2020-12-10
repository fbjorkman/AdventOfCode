import re

def recursiveCheck(bag):
	if goldBagRegex.match(bag):
		return True
	elif noBagRegex.match(bag):
		return False
	else:
		bag_contains = []
		connected_bags = str(kvstore.get(bag)).split(', ')
		for newbag in connected_bags:
			if goldBagRegex.match(newbag):
				approvedbags[bag] = None
				return True
			elif noBagRegex.match(newbag):
				continue
			if newbag[0] == '1':
				nextbag = newbag[2:] + 's'
			else:
				nextbag = newbag[2:]

			if nextbag in approvedbags:
				approvedbags[bag] = None
				return True
			if nextbag in disapprovedbags:
				continue

			bag_contains.append(recursiveCheck(nextbag))

		if True in bag_contains:
			approvedbags[bag] = None
		else:
			disapprovedbags[bag] = None
		return True in bag_contains


def main():
	f = open('day7input.txt')
	content = f.readlines()
	count = 0

	for line in content:
		temp = line.split(' contain ')
		kvstore[temp[0]] = temp[1].replace('\n', '').replace('.', '')
	for bag in kvstore.keys():
		if goldBagRegex.match(bag):
			continue
		recursiveCheck(bag)

	print('Number of bags that contains shiny gold bags: ', len(approvedbags))
	print('Number of bags that does not contains shiny gold bags: ', len(disapprovedbags))

goldBagRegex = re.compile('shiny gold bags?')
noBagRegex = re.compile('no other bags')
kvstore = dict()
approvedbags = dict()
disapprovedbags = dict()
main()