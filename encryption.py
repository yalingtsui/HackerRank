s = input()
l = len(s)
row = int(pow(l,0.5))
col = row + 1

matrix = []
if col * row < l:
	row = col
if row * row == l:
	col = row
print(row, col)
	
# for i in range(row):
# 	line = []
# 		#if i <= l / col:
# 	for j in range(col):
# 		if j <= l - 1 - col*i:
# 			line.append(s[col*i + j])
# 	matrix.append(line)

for i in range(row):
	matrix.append([])
	for j in range(col):
		if j <= l - 1 - col*i:
			matrix[i].append(s[col*i + j])
print(matrix)

newmatrix = []
for y in range(col):
	newline = ""
	for x in range(row):
		if l % col != 0:
			if x == row - 1  and y > (l % col) - 1:
				break
			else:
				newline += matrix[x][y]
		
		else:
			newline += matrix[x][y]
		
	newmatrix.append(newline)


print(" ".join(newmatrix))
