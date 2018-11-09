n = int(input()) 
string = []
for line in range(n):
	string.append(input().strip())




def bigger(s):


	if ord(s[-1]) > ord(s[-2]):
		return s[:-2] + s[-1] +s[-2]
	else:
		count += 1
		return bigger(s[:-1]) 

for s in string:
	print(bigger(s))

abcdef
abcdfe