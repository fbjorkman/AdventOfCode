import re

def main():
	f = open('day8input.txt')
	content = f.readlines()
	acc = 0
	i = 0
	index_list = []
	index_list.append(i)
	while True:
		if accRegex.match(content[i]):
			num = int(re.search(r'\d+', content[i]).group())
			if content[i][4] == '+':
				acc += num
			else:
				acc -= num
			if i+1 in index_list:
				return acc
			i += 1
			index_list.append(i)
		elif jmpRegex.match(content[i]):
			num = int(re.search(r'\d+', content[i]).group())
			if content[i][4] == '+':
				i += num
			else:
				i -= num
			if i in index_list:
				return acc
			index_list.append(i)
		elif nopRegex.match(content[i]):
			if i+1 in index_list:
				return acc
			i += 1
			index_list.append(i)

accRegex = re.compile('^acc')
jmpRegex = re.compile('^jmp')
nopRegex = re.compile('^nop')
print(main())