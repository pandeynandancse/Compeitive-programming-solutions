#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the swapToSort function below.
def swapToSort(a):
    # Return -1 or 0 or 1 as described in the problem statement.
    z=sorted(a)
    
    count = 0
    if z == a:
        return 0
    if z != a :
        print(len(z))
        for i in range(len(z)):
            if z[i]==a[i]:
                continue
            else:
                count = count + 1
    if count == 2:
        return 1
    else:
        return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = swapToSort(a)
    print(result)
    fptr.write(str(result) + '\n')

    fptr.close()
