# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head or k == 0:
            return head

        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        k = k % length
        if k == 0:
            return head

        one=head
        two=head

        for _ in range(k):
            two=two.next
        while two.next:
            one=one.next
            two=two.next
        new_head=one.next
        one.next=None
        two.next=head
        return new_head

        