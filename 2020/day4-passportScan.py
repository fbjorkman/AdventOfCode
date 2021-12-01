import re

def checkValidity(pass_string):
	if(re.search("byr", pass_string) == None):
		return False
	if(re.search("iyr", pass_string) == None):
		return False
	if(re.search("eyr", pass_string) == None):
		return False
	if(re.search("hgt", pass_string) == None):
		return False
	if(re.search("hcl", pass_string) == None):
		return False
	if(re.search("ecl", pass_string) == None):
		return False
	if(re.search("pid", pass_string) == None):
		return False
	return True

def main():
	f = open("day4input.txt")
	content = f.readlines()
	count = 0
	temp_string = ""

	for line in content:
		if(line != "\n"):
			temp_string += line
		else:
			if(checkValidity(temp_string)):
				count += 1
			temp_string = ""
	print(count)

main()