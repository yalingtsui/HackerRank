n, k = input().split()
p = ""
for i in range(int(k)):
	p += n

def superDight(p):
	if len(str(p)) == 1:
		return p
	else:
		new = 0
		for i in str(p):
			new += int(i)
			
		return superDight(new)

print(superDight(p))