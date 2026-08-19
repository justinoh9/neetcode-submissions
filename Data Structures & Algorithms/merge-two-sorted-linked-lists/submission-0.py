# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # example 1
        # 1, 2, 3
        # 4, 5, 6,
        # 1a, 2a, 3a, 4b, 5b, 6b

        # example 2
        # 
        # 1, 2, 3
        # 1b, 2b, 3b

        # example 3
        # 1, 8, 10
        # 6, 7, 9
        # 1a, 6b, 7b, 8a, 9b, 10a

        # 
        # headOne = list1
        # headTwo = list2
        # mergedCurr = None
        # mergedPrev = None
        # # basically, iterate through both lists until can't anymore
        # while headOne or headTwo:
        #     # case 1: if headOne is null or lower than headTwo
        #     if headOne == None or headOne.val < headTwo.val:
        #         mergedNext = headTwo
        #         mergedCurr = 

        dummy = ListNode()
        tail = dummy
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        
        return dummy.next