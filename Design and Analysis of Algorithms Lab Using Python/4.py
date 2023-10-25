def selection_sort(A):
  for i in range(len(A)-1):
    min_val = i
    for j in range(i+1,len(A)):
      if A[min_val] > A[j]:
        min_val = j
    A[i],A[min_val] = A[min_val],A[i]

n = int(input())
A = list(map(int,input().split()))
selection_sort(A)
print(' '.join(str(x) for x in A),"")
