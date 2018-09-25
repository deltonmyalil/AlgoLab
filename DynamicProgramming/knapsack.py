# 0/1 knapsack problem
W = 11 # maxWeight
wt = [1, 2, 5, 6, 7]
n = len(wt)
val = [1, 6, 18, 22, 28]
k = [[0 for x in range(W+1)]for x in range(n+1)] # col x row
for i in range(n+1):
	for w in range (W+1):
		if i==0 or w==0:
			k[i][w] = 0
			#print(i, w)
		elif wt[i-1] <= w:
			k[i][w] = max(val[i-1]+k[i-1][w-wt[i-1]], k[i-1][w])
		else:
			k[i][w] = k[i-1][w] # as prev
print(k[n][W])

