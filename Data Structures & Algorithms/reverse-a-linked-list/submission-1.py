# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        while curr:
            next_node = curr.next
            curr.next = prev
            curr.prev = next_node
            prev = curr
            curr = next_node

        return prev
            
        
        