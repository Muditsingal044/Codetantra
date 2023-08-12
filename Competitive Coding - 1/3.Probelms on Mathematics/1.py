import sys

n1 = int(sys.argv[1])
n2 = int(sys.argv[2])

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
  
def sumOfPrimes(n1, n2):
  l=[]
  if n2<n1:
    n3=n1
    n1=n2
    n2=n3
  for i in range(n1,n2):
    if isprime(i):
      l.append(i)
  return sum(l)

print(sumOfPrimes(n1, n2))
