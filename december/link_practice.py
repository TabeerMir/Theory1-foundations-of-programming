class LinkedNode:
    def __init__(self, data=None, next=None):
        self._data = data
        if next is None or isinstance(next,LinkedNode):
            self._next = next
        else:
            raise TypeError('node type object expected')
        
@property
def data(self):
    return self._data

@property
def tail(self):
    return self._next

@data.setter
def data(self,value):
    self._data = value

@tail.setter
def tail(self,node):
    if node is None or isinstance(node, LinkedNode):
        self._next = node
    else:
        raise TypeError('node type object expected')

class Linkedlist:
    def __init__(self):
        self.front = None
        self.tail = None
        self._size = 0
    
    def append(self, value):
        newnode = LinkedNode(value)
        if self._front is None:
            self._front = newnode
            self._tail = newnode
        else:
            self._tail.tail = newnode
            self._tail = newnode
        self._size +=1

    def pop(self):
        if self._size == 0:
            raise IndexError ('empty list')
        front_node = self._front
        self._front = self._front.tail
        front_node.tail = None
        self._size -=1
        return front_node.data

