# Coin exchange
coins = [1, 3, 4] 
n = len(coins)
amount = 6
# greedy gives soln [4, 1, 1]
# dp gives soln [3, 3]
table = [99999999 for i in range(amount+1)]
table[0] = 0
tab = [-1 for i in range(amount+1)]
j = 0
while j < len(coins):
	for i in range(amount + 1):
		if i >= coins[j]:
			if table[i] > table[i - coins[j]] + 1:
				table[i] = table[i - coins[j]] + 1
				tab[i] = j
	j += 1
i = amount
while i > 0:
	print(coins[tab[i]], end = ' ')
	i -= coins[tab[i]]
