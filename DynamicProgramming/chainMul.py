# import pandas as pd
A = [13, 5]
B = [5, 89]
C = [89, 3]
D = [3, 34]

P = [13, 5, 89, 3, 34]
# df = pd.DataFrame(index=2,columns=2)
# print(df)
n = len(P)
M = [[0 for x in range(n)] for x in range(n)]
bracket = [[0 for x in range(n)] for x in range(n)]


def printParantheses(i, j, n, bracket, name):
	if i == j:
		print(name)
		name += 1
		return
	print("(")
	printParantheses(i, bracket[i][j], n, bracket, name)
	printParantheses(bracket[i][j]+1, j, n, bracket, name)
	print(")")


# if i == j, then M[i,j] = 0
for i in range(1, n):
	M[i][i] = 0
# L is the chain length
for L in range(2, n):
	for i in range(1, n - L + 1):
		j = i + L - 1
		M[i][j] = 999999999
		for k in range(i, j):
			q = M[i][k] + M[k + 1][j] + P[i - 1] * P[k] * P[j]
			if q < M[i][j]:
				M[i][j] = q
				bracket[i][j] = k
print("individual Multiplications: ", M[1][n - 1])
name = 1
printParantheses(1, n - 1, n, bracket, name)
