import sys

arr = [int(x) for x in sys.argv[1].split(',')]

def sumHighestAndLowestElements(arr):
  max1 = max(arr)
  min1 = min(arr)
  return max1+min1

print(sumHighestAndLowestElements(arr))
