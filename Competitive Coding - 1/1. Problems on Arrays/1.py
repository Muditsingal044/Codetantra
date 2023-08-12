import sys

arr = [int(x) for x in sys.argv[1].split(',')]

def sumOfArray(arr):
  sum=0
  for i in arr:
    sum+=i
  return sum

print(sumOfArray(arr))
