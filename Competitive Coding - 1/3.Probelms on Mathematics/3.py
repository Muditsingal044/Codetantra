import sys

n = int(sys.argv[1])

def isprime(a):
  if a<2:
    return False
  if a==2:
    return True
  for i in range(2,a):
    if a%i==0:
      return False
  else:
    return True
  
def primeSum(n):
  l=[]
  for i in range(n1,n2):
    if isprime(i):
      l.append(i)
  sum1 = l[0]
  c = 0
  for i in range(1,len(l)):
    sum1+=l[i]
    if sum1<=n and isprime(sum1):
      c+=1
    if sum1>n:
      break
  return c
  
print(primeSum(n))
