def odd(tab): # ood man out function 
	for i in tab: 
		if tab.count(i) == 1:
			return i
		else:
			pass


n = int(input()) #nums of cases 
mydict = {} #case: man
for p in range(n):
	nums = int(input()) #nums of guests
	tab = [int(x) for x in input().strip().split()]
	man = odd(tab)
	mydict[p] = man

for i in mydict.keys():
	print("Case #{}: {}".format(int(i)+1, mydict[i]))

#2. 
# def odd(tab): # ood man out function 
# 	for i in tab: 
# 		if tab.count(i) == 1:
# 			return i
# 		else:
# 			pass


# n = int(input()) #nums of cases 
# for p in range(n):
# 	nums = int(input()) #nums of guests
# 	tab = [int(x) for x in input().strip().split()]
	
# 	print("Case #{}: {}".format(int(p)+1,odd(tab)))
