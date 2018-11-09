total = ""
while True:
	try:
		s = input().lower()
		line = s.strip()
		total = total + " " +line
	except EOFError:
		break

print(total)