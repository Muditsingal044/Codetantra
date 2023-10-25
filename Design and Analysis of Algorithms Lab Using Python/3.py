def insert_sort(A):
  for i in range(1,len(A)):
    key = A[i]
    j = i-1
    while j>=0 and key < A[j]:
      A[j+1] = A[j]
      j = i-1
    A[j+1] = key 
    
n = int(input())
A = list(map(int,input().split()))
insert_sort(A)
print(' '.join(str(x) for x in A),"")
