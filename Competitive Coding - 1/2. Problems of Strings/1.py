s = sys.argv[1]
l = int(sys.argv[2])

def getFirstSubString(s, l):
  s1=''
  l=0
  for i in range(l):
    try:
      s1+=s[l]
      l=l+2
    except:
      return 'NotFound'
  return s1

print(getFirstSubString(s, l))
