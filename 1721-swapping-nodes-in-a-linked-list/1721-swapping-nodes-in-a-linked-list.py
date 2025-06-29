# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        one=dummy
        two=dummy

        for i in range(k):
            two=   two.next

        first_node=two
        
        while two.next:
            one=one.next
            two=two.next

        second_node=one.next

        first_node.val, second_node.val = second_node.val, first_node.val

        return dummy.next     