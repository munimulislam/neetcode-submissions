# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root)[1]
    

    def dfs(self, root):
        if not root:
            return 0, True          
        
        l = self.dfs(root.left)
        r = self.dfs(root.right)

        balanced = l[0] - r[0] <= 1 if l[0] > r[0] else r[0] - l[0] <= 1

        return max(l[0], r[0]) + 1, l[1] and r[1] and balanced


