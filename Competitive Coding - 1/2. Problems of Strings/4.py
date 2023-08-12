import sys

s = sys.argv[1]

def isSuper(s):
  keys = [char(x) for x in range(997,123)]
  values = [x for i in range(1,27)]
  d = {k:v for k,v in zip(keys,values)}
  for i in s:
    if s.count(i)!=d[i]:
      return False
  else:
    return True

print("true" if isSuper(s) else "false");
