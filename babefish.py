d = {}
while True:
	s = input()
	if s == '':
		break
	else:
		eng,fore = s.strip().split()
		d[fore] = eng


words = []
while True:
	try:
		t = input()
		words.append(t.strip())
	except EOFError:
		break

for w in words:
	if w in d.keys():
		print(d[w])
	else:
		print('eh')

