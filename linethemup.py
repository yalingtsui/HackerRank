n = int(input())
name_letter = []
for line in range(n):
	name = input().strip()
	name_letter.append(name[0])


def increasing(L):
    """Returns TRUE if values in the list are increasing.
    Allows for values remaining constant. Does NOT allow null
    """
    return all(x<=y for x, y in zip(L, L[1:]))


def decreasing(L):
    """Returns TRUE if values in the list are decreasing.
    Allows for values remaining constant. Does NOT allow null
    """
    return all(x>=y for x, y in zip(L, L[1:]))

if increasing(name_letter) == True:
	print('INCREASING')
elif decreasing(name_letter) == True:
	print('DECREASING')
else:
	print('NEITHER')

# increasing = sorted(name_letter)
# decreasing = sorted(name_letter, reverse = True)
# if name_letter == increasing:
#     print("INCREASING")
# elif name_letter == decreasing:
#     print("DECREASING")
# else:
#     print("NEITHER")

def increasing(L):
    if len(L) <=1:
        return True
    else:
        if ord(L[0]) <= ord(L[1]):
            return increasing(L[1:])
        else:
            return False

def decreasing(L):
    if len(L) <=1:
        return True
    else:
        if ord(L[0]) >= ord(L[1]):
            return decreasing(L[1:])
        else:
            return False
if increasing(name_letter) == True:
  print('INCREASING')
elif decreasing(name_letter) == True:
  print('DECREASING')
else:
  print('NEITHER')


