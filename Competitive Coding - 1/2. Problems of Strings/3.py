import sys
s = sys.argv[1]
l = int(sys.argv[2])

def isEqualCharacters(s, l):
  stt = s[:l]
  rev = s[::-1]
  rev = rev[:l]
  if stt==rev:
    return True
  else:
    return False

print("true" if isEqualCharacters(s, l) else "false");
