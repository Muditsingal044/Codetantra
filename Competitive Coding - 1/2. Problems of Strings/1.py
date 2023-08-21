s = sys.argv[1]
l = int(sys.argv[2])

def getFirstSubString(s, l):
  s1=''
  l1=0
  for i in range(l):
    try:
      s1+=s[l1]
      l1=l1+2
    except:
      return 'NotFound'
  return s1

print(getFirstSubString(s, l))
