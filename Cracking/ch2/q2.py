# kth last element

# 1. Iterate through end and come back

from base import *


def kth(l: Node, k: int):
    while l._next != None:
        l = l._next

    for i in range(k):
        l = l._prev

    return l._data
