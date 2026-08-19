# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # basically, keep looping throuhg the cycle until it                   
        index = 0
        curr = head

        while index < 1000:
            if curr:
                curr = curr.next
            else:
                return False
            index += 1
        return True