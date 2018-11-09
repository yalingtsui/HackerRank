n = int(input())
if n == 0:
	print('EMPTY')
else:
	l = [int(x) for x in input().split()]
	new_l = []
	for i in l:
		new_l.append(-i)
	print(" ".join(str(e) for e in new_l))