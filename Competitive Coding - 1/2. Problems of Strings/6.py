import sys

S = sys.argv[1]

ch = 'QWERTYUIOPLKJHGFDSAZXCVBNMqwertyuioplkjhgfdsazxcvbnm'

def reverselAlphas(S):
  l=[]
  for i in S:
    if i in ch:
      l.append()
  s=''
  for i in S:
    if i in ch:
      s+=l.pop()
    else:
      s+=i
  return s
  
print(reverselAlphas(S));
