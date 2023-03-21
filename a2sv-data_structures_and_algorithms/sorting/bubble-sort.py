#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    swap = 0
    for i in a:
        for j in range(len(a) - 1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swap = swap + 1
                
    print("Array is sorted in {} swaps.\nFirst Element: {}\nLast Element: {}".format(swap, a[0], a[-1]))

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
