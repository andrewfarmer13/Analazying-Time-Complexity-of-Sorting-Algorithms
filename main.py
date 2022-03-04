# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 21:34:09 2022

@author: Clayton McEntire, Andrew Farmer, Cameron Burdine
"""
# Imports funcitons from other file
from bubble_merge import *
from quick_comb import *
import time
from matplotlib import pyplot as plt
from random import randint as ran

unsorted1 = [0]*1000
unsorted2 = [0] * 10000
unsorted3 = [0] * 30000


def generate(lists):
    temp = []
    for x in lists:
        temp.append(ran(1, 500))

    return temp


def main(unsorted1, unsorted2, unsorted3):
    # Test short list
    unsorted1 = generate(unsorted1)
    unsorted2 = generate(unsorted2)
    unsorted3 = generate(unsorted3)
    # dictionary to hold number of inputs and the time it took
    bubbleTime = []
    mergeTime = []
    combTime = []
    quickTime = []
    sizes = [1000, 10000, 30000]
   # print("Unsorted: "+ str(unsorted))

    # Test Bubble Sort
    print("\nBubble Sort:")
    time_start = time.perf_counter_ns()
    bubbleSort(unsorted1)
    time_end = time.perf_counter_ns()
    bubbleTime.append(time_end-time_start)
    print("Sorted: 1000, Time(in nanoseconds): " + str(time_end-time_start))
    time_start = time.perf_counter_ns()
    bubbleSort(unsorted2)
    time_end = time.perf_counter_ns()
    bubbleTime.append(time_end-time_start)
    print("Sorted: 10000, Time(in nanoseconds): " + str(time_end-time_start))
    time_start = time.perf_counter_ns()
    bubbleSort(unsorted3)
    time_end = time.perf_counter_ns()
    bubbleTime.append(time_end-time_start)
    print("Sorted: 30000, Time(in nanoseconds): " + str(time_end-time_start))

    # Test Merge Sort
    print("\nMerge Sort:")
    time_start = time.perf_counter_ns()
    merge_sort(unsorted1)
    time_end = time.perf_counter_ns()
    mergeTime.append(time_end-time_start)
    print("Sorted: 1000, Time(in nanoseconds): " + str(time_end-time_start))
    time_start = time.perf_counter_ns()
    merge_sort(unsorted2)
    time_end = time.perf_counter_ns()
    mergeTime.append(time_end-time_start)
    print("Sorted: 10000, Time(in nanoseconds): " + str(time_end-time_start))
    time_start = time.perf_counter_ns()
    merge_sort(unsorted3)
    time_end = time.perf_counter_ns()
    mergeTime.append(time_end-time_start)
    print("Sorted: 30000, Time(in nanoseconds): " + str(time_end-time_start))

    # Test Comb Sort
    print("\nComb Sort:")
    time_start = time.perf_counter_ns()
    combSort(unsorted1)
    time_end = time.perf_counter_ns()
    combTime.append(time_end-time_start)
    print("Sorted: 1000, Time(in nanoseconds): " + str(time_end-time_start))
    time_start = time.perf_counter_ns()
    combSort(unsorted2)
    time_end = time.perf_counter_ns()
    combTime.append(time_end-time_start)
    print("Sorted: 10000, Time(in nanoseconds): " + str(time_end-time_start))
    time_start = time.perf_counter_ns()
    combSort(unsorted3)
    time_end = time.perf_counter_ns()
    combTime.append(time_end-time_start)
    print("Sorted: 30000, Time(in nanoseconds): " + str(time_end-time_start))
    
    # Test Quick Sort
    n = len(unsorted1)
    print("\nQuick Sort:")
    time_start = time.perf_counter_ns()
    quickSort(unsorted1, 0, n-1)
    time_end = time.perf_counter_ns()
    quickTime.append(time_end-time_start)
    n = len(unsorted2)
    print("Sorted: 1000, Time(in nanoseconds): " + str(time_end-time_start))
    time_start = time.perf_counter_ns()
    quickSort(unsorted2, 0, n-1)
    time_end = time.perf_counter_ns()
    quickTime.append(time_end-time_start)
    print("Sorted: 10000, Time(in nanoseconds): " + str(time_end-time_start))
    n = len(unsorted3)
    time_start = time.perf_counter_ns()
    quickSort(unsorted3,0,n-1)
    time_end = time.perf_counter_ns()
    quickTime.append(time_end-time_start)
    print("Sorted: 100000, Time(in nanoseconds): " + str(time_end-time_start))

    # graph,messing around with graphing
    plt.style.use('seaborn-whitegrid')
    fig = plt.figure()
    ax = plt.axes()
    plt.xlabel("Number of Inputs")
    plt.ylabel("Time(s)")
    ax.set(xlim=(0, 40000), ylim=(0, 200000000))
    ax.plot(sizes, bubbleTime, color='g', label='Bubble Sort')
    ax.plot(sizes, mergeTime, color='b', label='Merge Sort')
    ax.plot(sizes, combTime, color='r', label='Comb Sort')
    ax.plot(sizes, quickTime, color='c', label='Quick Sort')
    ax.legend()
    plt.savefig("comparison_graph.png")


main(unsorted1, unsorted2, unsorted3)
