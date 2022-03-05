#!/bin/python3
#https://www.hackerrank.com/challenges/anagram/problem
import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#
def anagram(array1, array2):
    # Write your code here
    return_list = []

    for i in range(len(array1)):
        s1 = array1[i]
        s2 = array2[i]
        if (len(s1) != len(s2)):
            return_list.append(-1)
        else:
            dict1 = Counter(s1)
            dict2 = Counter(s2)
            changes = dict1-dict2
            return_list.append(sum(changes.values()))
    return return_list
if __name__ == '__main__':
    print(anagram(['tea', 'tea', 'act'], ['ate', 'toe', 'acts']))
'''
def anagram(s):
    # Write your code here
    if len(s)%2: #odd
        return -1
    else:
        half = (int)(len(s)/2)
        s1 = s[:half]
        s2 = s[half:]
        dict1 = Counter(s1)
        dict2 = Counter(s2)
        changes = dict1-dict2
        return sum(changes.values())
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
'''