
def knapsack(n, values, weights, capacity):

	dp = [[0 for x in range(capacity+1)] for y in range(n+1)]
	for i in range(1, n+1):
		for w in range(1, capacity+1):
      
			if weights[i-1] > w:
				dp[i][w] = dp[i-1][w]
			else:
				take = values[i-1] + dp[i-1][w-weights[i-1]]
				skip = dp[i-1][w]
				dp[i][w] = max(take, skip)
	return dp[n][capacity]
	
n = int(input())
values = list(map(int, input().split()))
weights = list(map(int, input().split()))
capacity = int(input())

max_value = knapsack(n, values, weights, capacity)
print(max_value)
