m, n, p, q = [int(x) for x in input().split()]

count = 0
for i in range(m + 1, n):
	if i % p == 0 and i % q == 0:
		count += i
	else:
		pass

print(count)