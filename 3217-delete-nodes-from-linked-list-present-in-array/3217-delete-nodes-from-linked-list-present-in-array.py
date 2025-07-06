# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        p=dummy
        my_set=set(nums)
        while p.next:
            if p.next.val in my_set:
                p.next=p.next.next
            else:
                p=p.next

        return dummy.next

        