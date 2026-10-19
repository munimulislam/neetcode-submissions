# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node_list = []
        curr = head
        while curr:
            node_list.append(curr)
            curr = curr.next

        if not node_list:
            return None

        head = node_list.pop()
        curr = head

        while node_list:
            curr.next = node_list.pop()
            curr = curr.next
        
        curr.next = None

        return head

        