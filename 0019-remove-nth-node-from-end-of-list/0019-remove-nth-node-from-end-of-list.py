# Definition for singly-linked list.
# class ListNode:

#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = slow = head
        # Move fast pointer n steps ahead
        for _ in range(n):
            fast = fast.next
        
        # If fast pointer reached the end, remove the head
        if not fast:
            return head.next
        
        # Move both pointers until fast reaches the end
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        # Skip the nth node
        slow.next = slow.next.next
        return head