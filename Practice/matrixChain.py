import sys

P = [13, 5, 89, 3, 34]
n = len(P)
m = [[0 for x in range(n)] for x in range(n)]

for i in range(1, n - 1):
	m[i][i] = 0  # if i == j, m[i][j] = 0
for l in range(2, n):
	for i in range(1, n - l + 1):
		j = i + l - 1
		m[i][j] = sys.maxsize
		for k in range(i,j):
			q = m[i][k] + m[k+1][j] + P[i-1]*P[k]*P[j]
			if q < m[i][j]:
				m[i][j] = q

print(m[1][n-1])
