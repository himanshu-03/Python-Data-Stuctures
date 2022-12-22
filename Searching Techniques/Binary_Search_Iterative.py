# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1r_ESNZfmsamM3vf802CW01GUvfLfgmjs

# Binary Search (Iterative)
"""

# Iterative Method
def binarysearch(a,key):
    start = 0
    end = len(a)-1

    while start <= end:

        mid = (start+end)//2

        if a[mid] == key:
            return mid

        elif a[mid] > key:
            end = mid - 1

        else:
            start = mid + 1

    return -1

a = []
size = int(input('Enter size of array: '))
print('')
for i in range(size):
    data = int(input('Enter element: '))
    a.append(data)
print('')
print('Elements are: ',a)

key = int(input('Enter key to search: '))

res = binarysearch(a,key)
if res == -1:
    print(key,'not found..!!')
else:
    print(key,'found at',res+1,'location')