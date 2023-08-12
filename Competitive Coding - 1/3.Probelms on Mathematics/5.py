import sys

N = int(sys.argv[1])
L = int(sys.argv[2])
R = int(sys.argv[2])

def sumBetween(N, L, R):
  a = [i for i in range(0,N+1,2)] + [i for i in range(1,N+2,2)]
  return sum(a[L:R+1])  

print(sumBetween(N, L, R))
