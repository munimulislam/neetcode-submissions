class ListNode:
    def __init__(self, val, nxt=None):
        self.value = val
        self.nxt = nxt

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    def get(self, index: int) -> int:
        i = 0
        current = self.head
        while i < index and current is not None:
            current = current.nxt
            i += 1
        
        return current.value if current is not None else -1
        

    def insertHead(self, val: int) -> None:
        node = ListNode(val, self.head)
        if self.tail is None:
            self.tail = node
        self.head = node
        

    def insertTail(self, val: int) -> None:
        node = ListNode(val)
        if self.tail is not None:
            self.tail.nxt = node
        self.tail = node
        if self.head is None:
            self.head = node
        

    def remove(self, index: int) -> bool:
        i = 0
        current = self.head
        previous = None
        while i < index and current is not None:
            previous = current
            current = current.nxt
            i += 1

        if current is None:
            return False
        
        if previous is None:
            self.head = current.nxt
            if self.tail is current:
                self.tail = current.nxt
            return True
        
        previous.nxt = current.nxt
        if self.tail is current:
            self.tail = previous if current.nxt is None else current.nxt
        return True

        

    def getValues(self) -> List[int]:
        values = []
        current = self.head
        while current is not None:
            values.append(current.value)
            current = current.nxt
        return values




        
