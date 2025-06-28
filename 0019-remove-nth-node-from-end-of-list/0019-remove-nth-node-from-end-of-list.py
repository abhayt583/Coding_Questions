# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head) 
        one = dummy
        two = dummy

        for i in range(n):
            two=two.next
        
        while two.next:
            one=one.next
            two=two.next
        
        one.next=one.next.next

        return dummy.next
        