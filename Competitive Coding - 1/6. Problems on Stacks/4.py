import sys
expr = sys.argv[1]

def get(c):
    if c=='-' or c=='+':
        return 1
    elif c=='*' or c=='/':
        return 2
    return 0
def infix(l):
    st=[]
    p=[]
    for x in l:
        if x=='(':
            st.append(x)
         if x in '+-/*':
             while True:
                 if get(x) <= get(st[-1]):
                     d = st.pop()
                     p.append(d)
                 else:
                     st.append(x)
                     break
         elif x==')':
             while True:
                 if st[-1!='(':
                     d = st.pop()
                     p.append(d)
                 else:
                     st.pop()
                     break
         else:
             p.append(x)
    return p

def evaluate(expr):
    e = '( '+expr+' )'
    e  = e.split(' ')
    t=[]
    for x in e[::-1]:
        if x =='(':
            t.append(')')
        elif x==')':
            t.append('(')
        else:
            t.append(x)
    res  = infix(t)
    ans=''
    res = res[::-1]
    for x in res:
        if x!=')' and x!='(':
            ans = ans +' '+x
    return ans[1:]

print(evaluate(expr))
