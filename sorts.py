from typing import List
import random



def create_random_list(length, max_value):
    L = []
    for _ in range(length):
        L.append(random.randint(0, max_value))
    return L



def selection_sort(L):
    for i in range(len(L)):
        min_index = find_min_index(L, i)
        L[i], L[min_index] = L[min_index], L[i]
        print(L)



def find_min_index(L, i):
    """
    Returns the index of the smallest number, starting from index i.

    >>> find_min_index([8,3,4,11], 0)
        1
    >>> find_min_index([8,2,4,11],2)
        2
    """
    min_index = i
    for j in range(i, len(L)):
        if L[j] < L[min_index]:
            min_index = j
    return min_index



def insert_into(L, i):
    """
    >>> L = [2,3,4,1,5]
    >>> insert_into(l, 3)
    >>> L
    [1,2,3,4,5]

    >>> insert_into([2,4,3,1,5], 2)
    >>> L
    [1,3,4,1,5]
    """
    while i > 0 and L[i] < L[i-1]:
        L[i], L[i-1] = L[i -1], L[i]
        i = i - 1



def insertion_sort(L):
    print(L)
    for i in range(len(L)):
        insert_into(L, i)
        print(L)



def bubble_sort(L):
    for j in range(len(L)):
        for i in range(len(L)-1):
            if L[1] > L[i+1]:
                L[i], L[i+1] = L[i+1], L[i]
    
