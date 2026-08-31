# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        # trend = []
        # current_num = head.val
        pos = 1
        pivot_pos = []
        while head.next and head.next.next:
            cur_trend = 1 if head.next.val > head.val else -1 if head.next.val < head.val else 0
            next_trend = 1 if head.next.next.val > head.next.val else -1 if head.next.next.val < head.next.val else 0
            if cur_trend * next_trend == -1:
                pivot_pos.append(pos)
            head = head.next
            pos += 1

        print(pivot_pos)
        if len(pivot_pos)<2:
            return [-1,-1]
        else:
            return [min([x-y for x,y in zip(pivot_pos[1:],pivot_pos[:-1])]),pivot_pos[-1]-pivot_pos[0]]