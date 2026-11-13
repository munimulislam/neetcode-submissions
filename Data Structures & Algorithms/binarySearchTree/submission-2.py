class Node:
    def __init__(self, key, val, left=None, right=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right

class TreeMap:
    
    def __init__(self):
        self.root = None


    def insert(self, key: int, val: int) -> None:
        self.root = self._insert(key, val, self.root)


    def _insert(self, key: int, val: int, root: Optional[Node]) -> Node:
        if not root:
            return Node(key, val)

        if root.key == key:
            root.val = val
        elif root.key < key:
            root.right = self._insert(key, val, root.right)
        else:
            root.left = self._insert(key, val, root.left)

        return root



    def get(self, key: int) -> int:
        curr = self.root

        while curr:
            if curr.key == key:
                return curr.val
            elif curr.key < key:
                curr = curr.right
            else:
                curr = curr.left
            
        return -1


    def getMin(self) -> int:
        node = self._getMin(self.root)
        return node.val if node else -1


    def _getMin(self, root: Optional[Node]) -> Optional[Node]:
        if not root:
            return None
        
        curr = root
        while curr.left:
            curr = curr.left
        
        return curr


    def getMax(self) -> int:
        if not self.root:
            return -1
        
        curr = self.root
        while curr.right:
            curr = curr.right
        
        return curr.val


    def remove(self, key: int) -> None:
        self.root = self._remove(key, self.root)

    
    def _remove(self, key: int, root: Optional[Node]) -> Node:
        if not root:
            return None
        
        if key == root.key:
            if not root.right:
                return root.left
            if not root.left:
                return root.right
            min_right = self._getMin(root.right)
            root.key = min_right.key
            root.val = min_right.val
            root.right = self._remove(root.key, root.right)

        elif key > root.key:
            root.right = self._remove(key, root.right)
        else:
            root.left = self._remove(key, root.left)

        return root


    def getInorderKeys(self) -> List[int]:
        return self._getInorderKeys(self.root)

    def _getInorderKeys(self, root: Optional[Node]) -> List[int]:
        if not root:
            return []
        
        return [*self._getInorderKeys(root.left), root.key, *self._getInorderKeys(root.right)]

