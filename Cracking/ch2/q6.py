from base import Node, LinkedListMaker, Print, bPrint
# Check to see if a linkedlist i palindrome or not?

l =  LinkedListMaker([1,2,3,4,2,1]).generate()

def p(h: Node):

    pe = h

    while pe._next != None:
        pe = pe._next

    ps = h

    while pe != ps:
        if pe._data != ps._data: return False

        pe = pe._prev
        ps = ps._next

    return True


print(p(l))