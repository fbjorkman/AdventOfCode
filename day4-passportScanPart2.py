import re

def checkByr(byr):
	if(byr == None or int(byr) < 1920 or int(byr) > 2002):
		return False
	return True

def checkIyr(iyr):
	if(iyr == None or int(iyr) < 2010 or int(iyr) > 2020):
		return False
	return True

def checkEyr(eyr):
	if(eyr == None or int(eyr) < 2020 or int(eyr) > 2030):
		return False
	return True

def checkHgt(hgt):
	if(hgt == None):
		return False
	if(re.search("in", hgt) != None):
		value = int(hgt[0:1])
		if(value < 59 and value > 76):
			return False
	elif(re.search("cm", hgt) != None):
		value = int(hgt[0:2])
		if(value < 150 and value > 193):
			return False
	else:
		return False
	return True
	

def checkValidity(pass_string):
	kvstore = dict()
	kvarray = pass_string.replace("\n", " ").split(" ")

	for kv in kvarray:
		temp = kv.split(":")
		if(len(temp) == 2):
			if(temp[0] == "ecl" and kvstore.get("ecl")):
				return False
			kvstore[temp[0]] = temp[1]

	if(not checkByr(kvstore.get("byr"))):
		return False
	if(not checkIyr(kvstore.get("iyr"))):
		return False
	if(not checkEyr(kvstore.get("eyr"))):
		return False
	if(not checkHgt(kvstore.get("hgt"))):
		return False
	if(kvstore.get("hcl") == None or not hclRegex.match(kvstore.get("hcl"))):
		return False
	if(not kvstore.get("ecl") in eye_color):
		return False
	if(kvstore.get("pid") == None or not pidRegex.match(kvstore.get("pid"))):
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

hclRegex = re.compile("^#[0-9a-f]{6}$")
eye_color = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
pidRegex = re.compile("[0-9]{9}")
main()