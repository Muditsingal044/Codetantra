import sys

s = sys.argv[1]

def isSuper(s):
  keys = [chr(x) for x in range(97,123)]
  values = [x for i in range(1,27)]
  d = {k:v for k,v in zip(keys,values)}
  for i in s:
    if s.count(i)!=d[i]:
      return False
  
  return True

print("true" if isSuper(s) else "false");
