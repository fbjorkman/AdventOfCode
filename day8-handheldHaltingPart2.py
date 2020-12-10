import re
from collections import deque

def main():
	f = open('day8input.txt')
	content = f.readlines()
	acc = 0
	i = 0
	index_list = []
	index_list.append(i)
	jmp_list = deque()
	nop_list = deque()

	for j in range(len(content)):
		if jmpRegex.match(content[j]):
			jmp_list.append(j)
		elif nopRegex.match(content[j]):
			nop_list.append(j)

	current = jmp_list.popleft()
	content[current] = content[current].replace('jmp', 'nop')
	count = 0
	while i != len(content):
		if accRegex.match(content[i]):
			num = int(re.search(r'\d+', content[i]).group())
			if content[i][4] == '+':
				acc += num
			else:
				acc -= num
			if i+1 in index_list:
				count += 1
				i = 0
				acc = 0
				index_list.clear()
				if len(jmp_list) > 0:
					content[current] = content[current].replace('nop', 'jmp')
					current = jmp_list.popleft()
					content[current] = content[current].replace('jmp', 'nop')
				else:
					content[current] = content[current].replace('jmp', 'nop')
					current = nop_list.popleft()
					content[current] = content[current].replace('nop', 'jmp')
			else:
				i += 1
				index_list.append(i)

		elif jmpRegex.match(content[i]):
			num = int(re.search(r'\d+', content[i]).group())
			if content[i][4] == '+':
				i += num
			else:
				i -= num
			if i in index_list or i < 0 or i > len(content):
				count += 1
				i = 0
				acc = 0
				index_list.clear()
				if len(jmp_list) > 0:
					content[current] = content[current].replace('nop', 'jmp')
					current = jmp_list.popleft()
					content[current] = content[current].replace('jmp', 'nop')
				else:
					content[current] = content[current].replace('jmp', 'nop')
					current = nop_list.popleft()
					content[current] = content[current].replace('nop', 'jmp')
			else:
				index_list.append(i)

		elif nopRegex.match(content[i]):
			if i+1 in index_list:
				count += 1
				i = 0
				acc = 0
				index_list.clear()
				if len(jmp_list) > 0:
					content[current] = content[current].replace('nop', 'jmp')
					current = jmp_list.popleft()
					content[current] = content[current].replace('jmp', 'nop')
				else:
					content[current] = content[current].replace('jmp', 'nop')
					current = nop_list.popleft()
					content[current] = content[current].replace('nop', 'jmp')
			else:
				i += 1
				index_list.append(i)
	print(content[current])
	return acc

accRegex = re.compile('^acc')
jmpRegex = re.compile('^jmp')
nopRegex = re.compile('^nop')
print(main())