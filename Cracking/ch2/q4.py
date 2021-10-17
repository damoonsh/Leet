# Partition

# Push values smaller than x to the left

from base import LinkedListMaker, Node, Print, bPrint
l = [3,5,8,5,10,2,1]

h = LinkedListMaker(l).generate()

def partition(h: Node, x: int):
    cop = h
    while h != None:
        if h._data > x and h._next == None: break
        if h._data > x and h._next._data < x:
            delNode = h._next

            # Delete the node
            if h._next._next != None:
                h._next._next._prev = h
            h._next = h._next._next

            h = h._prev
            # Find the place to put the node
            while True:
                if h._prev == None:
                    delNode._prev = None
                    delNode._next = h

                    h._prev = delNode
                    break
                else:
                    if h._prev._data >= x:
                        # print('22', h._data, h._prev._data)
                        h = h._prev
                    else:
                        delNode._prev = h._prev
                        delNode._next = h

                        h._prev._next = delNode
                        h._prev = delNode
                        
                        h = delNode
                        break
        else:
            h = h._next

    return h


p = partition(h, 5)

bPrint(p)
