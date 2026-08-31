# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        outputHead = ListNode(0)
        index = outputHead
        advance = 0
        while l1 or l2 or advance:
            n1 = l1.val if l1 else 0
            n2 = l2.val if l2 else 0


            index.next = ListNode((n1+n2+advance)%10)
            advance = (n1+n2+advance) // 10
            index = index.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        return outputHead.next