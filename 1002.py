import sys,array

sumLine = sys.stdin.readline()


def can_put(x,y,data,n):
    if data[x][y] == -1:
        return False
    j = n - 1
    while j >= 0:
        if data[x][j] == 1:
            return False
        elif data[x][j] == -1:
            break;
        j -= 1

    i = n - 1
    while i >= 0:
        if data[i][y] == 1:
            return False
        elif data[i][y] == -1:
            break;
        i -= 1

    return True
        
def findMax(position,n,data,currentSum):
    global currentMax
    
    if position < n * n:
        x = position/n
        y = position%n
        if can_put(x,y,data,n):
            #print "canput:%d %d" %(x,y) 
            data[x][y] = 1
            findMax(position + 1,n,data,currentSum + 1)
            data[x][y] = 0

        findMax(position +1 ,n,data,currentSum)
    else:
        if currentSum > currentMax:
            currentMax = currentSum 


while  sumLine and int(sumLine) > 0:
    line = int(sumLine)
    if line > 0 :
        currentMax = 0
        
        flags = [ [0 for i in range(line)] for j in range(line)]
        for i in range(0,line):
            content = sys.stdin.readline()
            
            for j in range(0,len(content) - 1):
                if content[j] == 'X':
                    flags[i][j] = -1
                else:
                    flags[i][j] = 0
                

   
        findMax(0,line,flags,0)
        print currentMax
    sumLine = int(sys.stdin.readline())




