# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # defnitely need a seen set
        seen = set()

        # most likely a while loop

        while head:
            if head.next in seen:
                return True
            else:

                seen.add(head.next)
                head = head.next

        return False