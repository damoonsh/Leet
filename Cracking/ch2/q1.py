class Node:
    def __init__(self, val):
        self._data = val
        self._next = None
        self._prev = None
    
    def appendToTail(self, tail):
        self._next = tail

    def appendToHead(self, head):
        self._prev = head

    def deleteNode(self):
        self._prev._next = self._next
        self._next._prev = self._prev
        


class LinkedListMaker:
    def __init__(self, vals):
        self._vals = vals

    def generate(self):
        for i in range(len(self._vals)):
            if  i == 0:
                head = Node(self._vals[i])
                prev = head
            else:
                newNode = Node(self._vals[i])
                prev.appendToTail(newNode)
                newNode.appendToHead(prev)

                prev = newNode

        return head

l = [1,10,9,5,4,10]

h = LinkedListMaker(l).generate()


# Question: In an unsorted linked list, how do we remove duplicates

# we get the first value then look through the rest of the 


def dups(l: Node):
    while l != None:
        if check(l._next, l._data):
            return True
        l = l._next
    return False

def check(l: Node, val: int):
    while l != None:
        if l._data == val: return True
        l = l._next

    return False
