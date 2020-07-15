#!/usr/bin/env python3

"""
Sort
"""

def insertion_sort(items):
    """ Insertion sort """
    for i in range(1, items.size()):
        j = i
        while j > 0 and items.get(j) < items.get(j - 1):
            temp = items.get(j - 1)
            items.set((j - 1), items.get(j))
            items.set(j, temp)
            j -= 1
    return items

def insertion_sort_r(items, i=1):
    """ Insertion sort recursion"""
    if i == items.size():
        return
    else:
        j = i
        while j > 0 and items.get(j) < items.get(j - 1):
            temp = items.get(j - 1)
            items.set((j - 1), items.get(j))
            items.set(j, temp)
            j -= 1
        insertion_sort_r(items, i + 1)
    return items

def bubble_sort(items):
    """ Bubble sort """
    for i in range(items.size()):
        for j in range(items.size()-1-i):
            if items.get(j) > items.get(j + 1):
                temp = items.get(j + 1)
                items.set((j + 1), items.get(j))
                items.set(j, temp)
    return items

def bubble_sort_r(items, i=0):
    """ Bubble sort recursion"""
    if i == items.size():
        return
    else:
        for j in range(items.size()-1-i):
            if items.get(j) > items.get(j + 1):
                temp = items.get(j + 1)
                items.set((j + 1), items.get(j))
                items.set(j, temp)
        bubble_sort_r(items, i + 1)
    return items
