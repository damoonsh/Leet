from base import Node, LinkedListMaker, Print, bPrint

l1 = LinkedListMaker([7,1,6]).generate()
l2 = LinkedListMaker([5,9,2]).generate()

def sum(h1: Node, h2: Node):
    s = Node(0)
    carry = 0
    while h1 != None or h2 != None:
        tmp = carry
        if h1 != None: tmp += h1._data
        if h2 != None: tmp += h2._data

        carry = tmp // 10
        tmp %= 10

        print(carry, tmp)
        s._data = tmp

        if h1._next == None and h2._next == None: break
        newNode = Node(0)
        newNode._prev = s
        s._next = newNode

        if s._prev == None:
            head = s

        s = s._next

        if h1 != None: h1 = h1._next
        if h2 != None: h2 = h2._next
        
        # Print(head)


    return head


Print(sum(l1,l2))
