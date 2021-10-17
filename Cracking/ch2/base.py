class Node:
    def __init__(self, val):
        self._data = val
        self._next = None
        self._prev = None
    
    def appendToTail(self, tail):
        self._next = tail

    def appendToHead(self, head):
        self._prev = head
        


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

def Print(h: Node):
    while h != None:
        print(h._data, ' ',end='')
        h = h._next
    print()

def bPrint(h: Node):
    while h != None:
        print(h._data, ' ',end='')
        h = h._prev
    print()    
l = [1,10,9,5,4,10]

h = LinkedListMaker(l).generate()