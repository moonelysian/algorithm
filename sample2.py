#!/bin/python3

import math
import os
import random
import re
import sys


l = int(input())
r = int(input())

# Complete the oddNumbers function below.
def oddNumbers(l, r):
    if l%2 is 0:
        for i in range(l+1,r+1,2):
            print(i)
    else:
        for i in range(l,r+1,2):
            print(i)

oddNumbers(l, r)