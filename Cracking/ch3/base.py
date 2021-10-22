class Node:
    def __init__(self, data):
        self._data = data
        self._next = None


class Stack:
    def __init__(self):
        self._top = None

    def push(self, val):
        newNode = Node(val)
        if self._top == None: 
            self._top = newNode
        else:
            newNode._next = self._top
            self._top = newNode

    def pop(self):
        item = self._top._data
        self._top = self._top._next

        return item
    
    def isEmpty(self): return self._top == None

    def peek(self): 
        if self.isEmpty(): 
            return None
        else:
            return self._top._data


class Queue:
    def __init__(self):
        self._first: Node = None
        self._last: Node = None

    def add(self, val):
        newNode = Node(val)
        if last != None: last._next = newNode
        last = newNode

        if first == None: first = newNode

    def remove(self):
        if self._first == None: return None

        data = self._first._data

        self._first = self._first._next
        if self._first == None: last = None

        return data

    def peek(self):
        if self._first != None: return self._first._data

        return None

    def isEmpty(self): return self._first == None



