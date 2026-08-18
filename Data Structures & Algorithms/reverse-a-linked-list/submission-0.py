# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr: # while the current node exists
            temp = curr.next # create a temporary node for the value of the next node
            curr.next = prev # set the previous node to the next node
            prev = curr # set the previous node value to the value of the current node
            curr = temp # finally, change the value of the current node to the value of the next node
        return prev # return the last node

