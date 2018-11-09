# n = int(input())
# d = {}
# l = [int(i) for i in input().split()]
# for i in range(n):
# 	d[i] = l[i]

# n_l = []
# for item in l:
# 	if l.count(item) == 1:
# 		n_l.append(item)
# 	else:
# 		pass

# if len(n_l) == 0:
# 	print('none')
# 	exit()
# high = max(n_l)
# index = list(d.values()).index(high)
# index_d = list(d.keys())[index] + 1
# print(index_d)

n = int(input())
l = [int(i) for i in input().split()]

n_l = []
for item in l:
	if l.count(item) == 1:
		n_l.append(item)
	else:
		pass

if len(n_l) == 0:
	print('none')
	exit()

high = max(n_l)
index = l.index(high) + 1
print(index)

