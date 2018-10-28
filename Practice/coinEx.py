amt = int(input("Enter amount>>>"))
den = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
toGive = []
cur = 0
i = 0
for note in den:
	while cur < amt:
		if cur + note > amt:
			break
		cur += note
		toGive.append(note)
	if cur > amt:
		break
print(toGive)
