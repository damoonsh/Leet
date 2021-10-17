# Delete the middle node

from base import *


def mid(l: Node):
    p1 = l
    p2 = l._next

    while p2 != None:
        p1 = p1._next

        if p2._next != None: p2 = p2._next
        else: break
        p2 = p2._next

    # removing part
    p1._prev._next = p1._next
    p1._next._prev = p1._prev

    while p1._prev != None:
        p1 = p1._prev

    return p1