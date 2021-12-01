import itertools
import time

def main():
	f = open("day1input.txt","r")
	content = f.readlines()
	for f1 in content:
		for f2 in itertools.islice(content, content.index(f1), None):
			for f3 in itertools.islice(content, content.index(f2), None):
				f1 = int(f1)
				f2 = int(f2)
				f3 = int(f3)
				if(f1+f2+f3 ==2020):
					print(f1,f2,f3)
					print(f1*f2*f3)

start_time = time.time()
main()
print(time.time()-start_time)