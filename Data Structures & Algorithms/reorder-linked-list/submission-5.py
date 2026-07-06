# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        #find middle of list
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        #slow is now in the middle, and we split the list and reverse the second half
        curr = slow.next
        slow.next = None
        prev = None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        #first starts at head of first list
        #second starts at head of second list(reversed)
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

        
        
        
        
        