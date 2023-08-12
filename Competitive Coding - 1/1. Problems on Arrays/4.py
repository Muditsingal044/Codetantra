import sys

arr = [int(x) for x in sys.argv[1].split(',')]

def maxSumContiguousSubArray(arr):
  sum1 = 0
  ans = 0
  for i in range(len(arr)):
    sum1+= arr[i]
    if sum1<0:
      sum1 = 0
    elif ans < sum1:
      ans = sum1
  return ans 

print(maxSumContiguousSubArray(arr))
