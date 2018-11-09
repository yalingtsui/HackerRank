#1.
# score_sum = []
# for line in range(5):
# 	score = [int(x) for x in input().strip().split()]
# 	score_sum.append(score)

# point = []
# for i in score_sum:
# 	point.append(sum(i))

# high = max(point)
# num = point.index(high) + 1
# print(num, high)

#2.
# mydict = {}
# for line in range(5):
# 	score = [int(x) for x in input().strip().split()]
# 	sumscore = sum(score)
# 	mydict[line] = sumscore

# high = max(mydict.values())
# ikey = [key for (key, value) in mydict.items() if value == high]
# for i in ikey:
# 	x = int(i)
# print(x + int(1), high)

#3.
mydict = {}
for line in range(5):
	mydict[line] = sum([int(x) for x in input().strip().split()])
high = max(mydict.values())
num = list(mydict.keys())[list(mydict.values()).index(high)]
print(num + 1, high)