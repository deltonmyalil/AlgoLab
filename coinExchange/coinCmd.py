# Coin Exhange program
# Delton Myalil Antony, 18MCMI05
import sys
# amt = int(input("Enter the amount to be paid>>>"))
# f = open("data.txt", "r")
amt = int(sys.argv[1])#int(f.readline())
# sys.argv[0] is the filename itself
print("Amount of {0} read from the command line".format(amt))
if amt < 0:
	print("Error")
den = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
toGive = []
cur = int(0)
i = int(0)
vectorIndex = 0
solnVector = [0,0,0,0,0,0,0,0,0,0]
for note in den:
	while(cur < amt):
		if cur + note > amt:
			break
		cur += note
		toGive.append(note)
		solnVector[vectorIndex] += 1
	if cur > amt:
		break
	vectorIndex += 1
if amt >= 0:
	out = open("output.txt", 'w')
	out.write(str(solnVector))
	print(toGive)
	print("Rupees {0} paid in {1} number of notes".format(cur, len(toGive)))
	print("Solution Vector: ", solnVector)
	print("Written output to file output.txt")