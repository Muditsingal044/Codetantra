expr = sys.argv[1]

def evaluate(expr):
  expr = expr.split(" ")
  s=[]
  for i in expr:
    if i not in "+-/*:
        s.insert(0,i)
    else:
        op1 = s[0]
        s.pop(0)
        op2 = s[0]
        s.pop(0)
        if i in "*/":
            if "+" in op2 or "-" in op2:
                if '+' in op1 or '-' in op1:
                    s.insert(0,'('+op2+') ' +i+' ('+op1+')')
                else:
                    s.insert(0,'('+op2+') '+i+" "+op1)
            elif '+' in op1 or '-' in op1:
                    s.insert(0,op2+' '+i' ('+op1+')')
            else:
                    s.insert(0,op2+' '+i+' '+op1)
        else:
            s.insert(0,op2+' '+i+' '+op1)

  return s[0]

print(evaluate(expr))
        
    
