#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    minsum = sum - max(arr)
    maxsum = sum - min(arr)
    print (minsum, maxsum)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
