import sys

arr = [int(x) for x in sys.argv[1].split(',')]

def pairsOfSum(arr , s):
  ans = ''
  for i in range(len(arr)):
    for j in range(i+1,len(arr)):
      if arr[i]+arr[j] == s and i!=j:
        ans+='<'+str(i)+','+str(j)+'>'+','
  if len(ans):
    return ans[:-1]
  else:
    return 'no such pairs'

print(pairsOfSum(arr, s))
