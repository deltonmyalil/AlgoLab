# Coin Exhange program
# Delton Myalil Antony, 18MCMI05

amt = int(input("Enter the amount to be paid>>>"))
if amt < 0:
	print("Error")
den = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
toGive = []
cur = int(0)
i = int(0)
for note in den:
	while(cur < amt):
		if cur + note > amt:
			break
		cur += note
		toGive.append(note)
	if cur > amt:
		break
if amt >= 0:
	print(toGive)
	print("Rupees {0} paid in {1} number of notes".format(cur, len(toGive)))