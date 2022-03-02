# -*- coding: utf-8 -*-
"""
Created By: Clayton McEntire

Sorts In File
Merge Sort / Bubble Sort

"""


# Bubble Sort Algorithm
# Best Case O(n^2)
#=============================================================================
def bubbleSort(myList): 
    for i in range(len(myList)-1):
        for j in range(len(myList)-i-1):
            if myList[j] > myList[j + 1]:
                myList[j], myList[j+1] = \
                            myList[j + 1], myList[j]
    return myList
#=============================================================================

# Merge Sort Algorithm 
# Best Case O(n log(n))
#=============================================================================
def merge_sort(m):
    if len(m) <= 1:
        return m
 
    middle = len(m) // 2
    left = m[:middle]
    right = m[middle:]
 
    left = merge_sort(left)
    right = merge_sort(right)
    return list(merge(left, right))

def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0
    while left_idx < len(left) and right_idx < len(right):
        # change the direction of this comparison to change the direction of the sort
        if left[left_idx] <= right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
 
    if left_idx < len(left):
        result.extend(left[left_idx:])
    if right_idx < len(right):
        result.extend(right[right_idx:])
    return result
#=============================================================================