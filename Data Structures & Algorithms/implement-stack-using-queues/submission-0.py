class Node:
    def __init__(self, val = None, next = None, previous = None):
        self.val = val
        self.next = next
        self.previous = previous


class Queue:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.previous = self.head
        self.length = 0

    def size(self):
        return self.length
    
    def isEmpty(self):
        return self.length == 0

    def enqueue(self, value):
        node = Node(value, self.tail, self.tail.previous)
        node.previous.next = node
        node.next.previous = node
        self.length += 1

    def dequeue(self):
        if self.isEmpty():
            return None
        
        curr = self.head.next
        tmp = curr.val
        curr.next.previous = curr.previous
        curr.previous.next = curr.next
        self.length -= 1
        return tmp

    def peek(self):
        if self.isEmpty():
            return None

        return self.head.next.val


class MyStack:

    def __init__(self):
        self.queue = Queue()

    def push(self, x: int) -> None:
        length = self.queue.size()

        if length == 0:
            self.queue.enqueue(x)
            return

        self.queue.enqueue(x)

        while length:
            val = self.queue.dequeue()
            self.queue.enqueue(val)
            length -= 1


    def pop(self) -> int:
        return self.queue.dequeue()
        

    def top(self) -> int:
        return self.queue.peek()
        

    def empty(self) -> bool:
        return self.queue.size() == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()