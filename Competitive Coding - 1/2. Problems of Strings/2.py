import sys
s = sys.argv[1]


def isPrimeLengthPalidroms(s):
  f = 0
  a = len(s)
  for i in range(2,a):
    if a%i==0:
      f=1
      break
  if s==s[::-1] and f==0:
    return True
  else:
    return False

print(isPrimeLengthPalidroms(s))
