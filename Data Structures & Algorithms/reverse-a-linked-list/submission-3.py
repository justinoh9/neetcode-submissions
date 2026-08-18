# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # iteratively
        # we do this through a two pointer approach
        curr = head
        prev = None

        while curr: # so as long as curr isn't null, the loop will run
            # we create a temporary variable "temp" to store the value of the next node
            temp = curr.next
            # now, we switch the direction of the current node pointer to the previous node
            curr.next = prev
            # then, we change the value of the previous node to the current node
            prev = curr
            
            
            
            # after that, set current node value equal to the next node value
            curr = temp

        return prev