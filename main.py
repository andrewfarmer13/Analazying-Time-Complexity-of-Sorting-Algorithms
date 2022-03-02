# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 21:34:09 2022

@author: Clayton
"""
# Imports funcitons from other file
from bubble_merge import *

# Test short list 
unsorted = [1,9,5,6,2]

print("Unsorted: "+ str(unsorted))

# Test Bubble Sort
print("\nBubble Sort:")
sortedlist = bubbleSort(unsorted)
print("Sorted: " + str(sortedlist))

unsorted = [1,9,5,6,2] 

# Test Merge Sort
print("\nMerge Sort:")
sortedlist = merge_sort(unsorted)
print("Sorted: " + str(sortedlist))