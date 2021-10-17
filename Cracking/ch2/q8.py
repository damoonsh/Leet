# Loopd etection


from base import Node, LinkedListMaker, Print, bPrint

l = LinkedListMaker([1,2,3,4,5,3]).generate()

def findLoop(l: Node):
    while l != None:
        l = l._next
        if findVal(l._prev, l._data): return l._data

    return -1

def findVal(l: Node, val: int):
    while l != None:
        if l._data == val: return True

        l = l._prev

    return False

    
print(findLoop(l))