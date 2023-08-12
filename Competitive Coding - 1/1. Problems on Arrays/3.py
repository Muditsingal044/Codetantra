import sys

arr = [int(x) for x in sys.argv[1].split(',')]

def middleElementOfArray(arr):
  l = len(arr) - 1
  return arr[l//2]

print(middleElementOfArray(arr))
