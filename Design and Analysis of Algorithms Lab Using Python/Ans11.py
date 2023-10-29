
def longest_common_subsequence(str1, str2):
	m = len(str1)
	n = len(str2)

	table = [[0] * (n+1) for i in range(m+1)]                  
	for i in range(1, m+1):
		for j in range(1, n+1):
			if str1[i-1] == str2[j-1]:
				table[i][j] = table[i-1][j-1] + 1
			else:
				table[i][j] = max(table[i-1][j], table[i][j-1])    
	return table[m][n]
	

str1 = input().strip()
str2 = input().strip()
result = longest_common_subsequence(str1, str2)
print(result)
