import sys

expr = sys.argv[1]

def evaluate(expr):
	l = []
	s = s.split()
	for i in s:
		if i not in "+-*/":
			l.append(i)
		else:
      a = l.pop()
			b = l.pop()
			l.append(str(int(eval(b+i+a))))
	return l.pop()

print(evaluate(expr))
