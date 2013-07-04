import sys



def printRslt(rst):
    if len(rst) > 0:
        print(' '.join(rst))

def stackMatch(a1,a2,rslt,temp,i,j):
    if j == len(a2):
        printRslt(rslt)
        return;
    if i < len(a1):
        rslt.append("i")
        temp.append(a1[i])
        
        stackMatch(a1,a2,rslt,temp,i + 1 ,j)
        
        rslt.pop()
        temp.pop()
    if len(temp) > 0:
        top = temp[-1]
        if top == a2[j]:
            rslt.append("o")
            temp.pop()
            
            stackMatch(a1,a2,rslt,temp,i,j + 1)
            
            rslt.pop()
            temp.append(top)

a1 = sys.stdin.readline()
while a1 :
    a2 = sys.stdin.readline()
    print "["
    if len(a1) == len(a2) and len(a1) > 0 :
        stackMatch(a1.rstrip('\n'),a2.rstrip('\n'),[],[],0,0)
    print "]"




    a1 = sys.stdin.readline()