import sys

arr = [int(x) for x in sys.argv[1].split(',')]

def lengthIndexMatch(arr):
  s=''
  for i in range(len(arr)):
    if i==len(arr[i]):
      s+=arr[i]
  if len(s):
    return s
  else:
    return 'no match found'

print(lengthIndexMatch(arr))
