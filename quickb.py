n = int(input())
listb = []
listb = [chr(i) for i in range(ord('a'), ord('z')+1)]
setb = set(listb)
result = []

for line in range(n):
	seta = set(list(input().lower()))
	set_ = setb - seta
	list_ = list(set_)
	list_.sort()
	s = "".join(list_)

	if s == "":
		result.append('pangram')
	else:
		result.append("missing {}".format(s))

for r in result:
	print(r)


