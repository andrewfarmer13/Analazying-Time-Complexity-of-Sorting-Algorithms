# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 21:34:09 2022

@author: Clayton McEntire, Andrew Farmer, 
"""
# Imports funcitons from other file
from bubble_merge import *
import time
from matplotlib import pyplot as plt


# Test short list 
unsorted = [1,9,5,6,2]
##delete this, this is just for testin the graph
test_list = [10, 20,30,40,50]

print("Unsorted: "+ str(unsorted))

# Test Bubble Sort
print("\nBubble Sort:")
time_start = time.perf_counter_ns()
sortedlist = bubbleSort(unsorted)
time_end = time.perf_counter_ns()
print("Sorted: " + str(sortedlist) + ", Time(in nanoseconds): " + str(time_end-time_start))

unsorted = [1,9,5,6,2] 

# Test Merge Sort
print("\nMerge Sort:")
time_start = time.perf_counter_ns()
sortedlist = merge_sort(unsorted)
time_end = time.perf_counter_ns()
print("Sorted: " + str(sortedlist)+ ", Time(in nanoseconds)" + str(time_end - time_start))

## graph
plt.style.use('seaborn-whitegrid')
fig = plt.figure()
ax = plt.axes()
plt.xlabel("Number of Inputs")
plt.ylabel("Time(ns)")
ax.set(xlim =(0,10), ylim=(0,70))
ax.plot(sortedlist,test_list, color='g')
plt.savefig("comparison_graph.png")


