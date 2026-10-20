class Node:
    def __init__(self, url: str, next: Node = None, previous: Node = None):
        self.url = url
        self.next = next
        self.previous = previous


class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Node(None)
        self.tail = Node(None)
        node = Node(homepage, self.tail, self.head)
        self.head.next = node
        self.tail.previous = node
        self.current = node


    def visit(self, url: str) -> None:
        node = Node(url, self.tail, self.current)
        self.tail.previous = node
        self.current.next = node
        self.current = node
        

    def back(self, steps: int) -> str:
        curr = self.current

        while curr is not self.head:
            if steps == 0:
                self.current = curr
                return curr.url
            curr = curr.previous
            steps -= 1

        self.current = self.head.next
        return self.current.url
        

    def forward(self, steps: int) -> str:
        curr = self.current

        while curr is not self.tail:
            if steps == 0:
                self.current = curr
                return curr.url
            curr = curr.next
            steps -= 1
        
        self.current = self.tail.previous
        return self.current.url
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)