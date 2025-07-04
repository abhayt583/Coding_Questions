# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr =head
        for i in range(k-1):
            curr=curr.next
        
        fast,slow=head,head

        for i in range (k-1):
            fast=fast.next
        
        while fast.next:
            fast,slow=fast.next,slow.next
        
        curr.val,slow.val=slow.val,curr.val
        return head