M = 5  # capacity
wt = [3, 2, 4, 1]
val = [100, 20, 60, 40]
n = len(wt)
V = [[0 for x in range(M + 1)] for x in range(n + 1)]
for i in range(n + 1):
	for w in range(M + 1):
		if i == 0 or w == 0:
			V[i][w] = 0
		elif wt[i - 1] <= w:
			V[i][w] = max(V[i - 1][w], val[i - 1] + V[i - 1][w - wt[i - 1]])
		else:
			V[i][w] = V[i - 1][w]  # as prev
for i in V:
	print(i)
print(V[n][M])
