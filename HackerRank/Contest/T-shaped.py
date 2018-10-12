import math
import os
import random
import re
import sys

def solve(grid):
    lia=[]
    lib=[]
    li=[]
    c=[]
    ca=[]
    for b in grid:
            lia.append(b[0])
            lib.append(b[1])
     
    b = set()
    a = set()
    for m in grid:
            a.add(m[0])
            b.add(m[1])
   
    x = list(a)
    y = list(b)
    x.sort()
    y.sort()
    for l in x:
        c.append(lia.count(l))
    
    
    for d in y:
        ca.append(lib.count(d))
    

    it = 0
    itb = 0
    for i in range(len(x)):
        if(it<len(x)-1):
            if(i+1<len(x)):
                if x[i] == x[i+1]-1:
                    it = it + 1
                    
    
    for k in range(len(y)):
        if(itb<len(y)-1):
            if(k+1<len(x)):
                if y[k] == y[k+1]-1:
                    itb = itb + 1
                   
        
    if it == len(x)-1 and itb == len(y)-1:
        if(c[0]==3):
            if(ca[1]==3):
                return("Yes")
            
            else:
                return("No")
            
        
        elif(c[1]==3):
            if(ca[0]==3):
                return("Yes")
           
            elif(ca[2]==3):
                return("Yes")
           
            else:
                return("No")
            
        
        elif(c[2]==3):
            if(ca[1]==3):
                return("Yes")
            
            else:
                return("No")
    else:
        return("No")
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        points = []

        for _ in range(5):
            points.append(list(map(int, input().rstrip().split())))

        result = solve(points)
        fptr.write(result + '\n')
        

    fptr.close()
