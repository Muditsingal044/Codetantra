import sys
s = sys.argv[1]
l = int(sys.argv[2])

def isEqualCharacters(s, l):
  s = s[:l]
  rev = s[::-1]
  rev = rev[:l]

if s==rev:
  return True
else:
  return False

print("true" if isEqualCharacters(s, l) else "false");
