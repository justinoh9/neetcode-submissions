# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        '''
        brute force
        iterate through each linked list, storing nodes in a seperate array
        once each linked list is stored, sort the array's nodes by their value
        relink each node to create a new linked list
        '''
        # time complexity of above approach: O(m + nlog(k))
        # space: O(n)

        # bf
        nodeArr = []
        # maybe store a tuple, (node, node.val) and sort node.val

        for linkedList in lists:
            node = linkedList
            while node:
                nodeArr.append((node, node.val))
                node = node.next
        # arr.sort(key=lambda x: x[1])
        nodeArr.sort(key=lambda x: x[1])

        # link arr

        dummy = ListNode()
        curr = dummy
        for node, nodeVal in nodeArr:
            curr.next = node
            curr = curr.next
        return dummy.next


        