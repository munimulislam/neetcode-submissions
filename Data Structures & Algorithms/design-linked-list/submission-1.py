class ListNode:
    def __init__(self, value, nxt=None, prev=None):
        self.value = value
        self.next = nxt
        self.prev = prev

class MyLinkedList:

    def __init__(self):
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0
        while curr is not self.tail:
            if i == index:
                return curr.value
            curr = curr.next
            i += 1
            
        return -1

        

    def addAtHead(self, val: int) -> None:
        node = ListNode(val, self.head.next, self.head)
        self.head.next.prev = node
        self.head.next = node
        

    def addAtTail(self, val: int) -> None:
        node = ListNode(val, self.tail, self.tail.prev)
        self.tail.prev.next = node
        self.tail.prev = node
        

    def addAtIndex(self, index: int, val: int) -> None:
        i = 0
        curr = self.head.next
        while curr:
            if i == index:
                node = ListNode(val, curr, curr.prev)
                curr.prev.next = node
                curr.prev = node
                return
            
            i += 1
            curr = curr.next
        

    def deleteAtIndex(self, index: int) -> None:
        i = 0
        curr = self.head.next
        while curr is not self.tail:
            if i == index:
                curr.prev.next = curr.next
                curr.next.prev = curr.prev
                curr.next = None
                curr.prev = None
                return
            
            i += 1
            curr = curr.next
        
            
        
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)