import sys

expr = sys.argv[1]

def evaluate(expr):
	l = []
	s = expr.split()
	s = s[::-1]
	for i in s:
		if i not in "+-*/":	
			l.append(i)	
		else:	
			a = l.pop()	
			b = l.pop()
			l.append(str(int(eval(a+i+b))))
	return l.pop()

print(evaluate(expr))
