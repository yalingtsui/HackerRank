
res = []

while True:
	s = input()
	if s == "0 0":
		break

		# # else:
	a, b = [int(x) for x in s.strip().split()]
	inte = int(a / b)
	res.append((inte, "{} / {}".format(a - inte*b, b)))

for r in res:
	print(r[0], r[1])