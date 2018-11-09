length = []
while True:
	try:
		s = input()
		if s == "":
			break
		line = s.strip()
		l = len(line)
		length.append(l)
	except:
		break
cha = 0
longest = max(length)
for l in length:
	if l == longest:
		pass
	else:
		cha += (longest - l) * (longest - l)
	

result = cha - pow((length[-1] - longest),2)
print(result)

