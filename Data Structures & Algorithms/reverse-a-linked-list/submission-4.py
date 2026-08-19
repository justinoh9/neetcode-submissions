# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # need to change the direction of each pointer 
        # can do this recursively or iteratively
        # i think i like the iterave approach more, i kind of understand it

        currentNode = head
        prevNode = None

        while currentNode:
            # first, store the nextNode
            nextNode = currentNode.next
            # then, set the currentNode pointer to previousNode
            currentNode.next = prevNode
            # then, set previousNode = currentNode
            prevNode = currentNode
            # finally, set the current node to the next node
            currentNode = nextNode
        return prevNode