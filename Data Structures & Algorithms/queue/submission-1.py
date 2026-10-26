class Node:
    def __init__(self, val = None, nxt = None, prev = None):
        self.val = val
        self.next = nxt
        self.previous = prev

class Deque:
    
    def __init__(self):
        self.head = self.tail = Node()


    def isEmpty(self) -> bool:
        return self.head is self.tail
        

    def append(self, value: int) -> None:
        node = Node(value)
        self.tail.next = node
        node.previous = self.tail
        self.tail = node
        

    def appendleft(self, value: int) -> None:
        node = Node(value, self.head.next, self.head)
        self.head.next = node

        if self.isEmpty():
            self.tail = node
        else:
            node.next.previous = node
        

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        
        tmp = self.tail.val
        self.tail.previous.next = None
        self.tail = self.tail.previous
        return tmp


    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        
        curr = self.head.next
        tmp = curr.val
        self.head.next = curr.next
        if curr is self.tail:
            self.tail = self.head
        else:
            curr.next.previous = self.head

        return tmp
        
