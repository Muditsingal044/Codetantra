treeStr = sys.argv[1]
s = int(sys.argv[2])

def hasSum(treeStr,s):
    tree = treeStr.split(' ')
    ch = [0]
    curr = [s]
    while True:
        a = []
        new = []
        for x in range(len(ch)):
            to = curr[x]-int(tree[ch[x]])
            i = 2*ch[x]+1
            f1 = 0
            if i<len(tree):
                if tree[i]=='-':
                    f1 = 1
                else:
                    a.append(i)
                    new.append(to)
            else:
                f1 = 1
            f2 = 0
            j = 2*ch[x]+2
            if j<len(tree):
                if tree[j]=='-':
                    f2 = 1  
                else:
                    a.append(j)
                    new.append(to)
            else:
                f2 = 1
            if f1==1 and f2==1 and to == 0: 
                return True
        if len(a)==0:
            return False
        ch=[]
        for x in range(0,len(a)):
            ch.append(a[x])
        curr=[]
        for x in range(0,len(new)):
            curr.append(new[x])
    return False

print('true' if hasSum(treeStr, s) else 'false');
  
