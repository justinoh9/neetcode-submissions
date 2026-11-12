# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        arr1, arr2 = [], []

        node = l1
        while node:
            arr1.append(node.val)
            node = node.next

        node = l2
        while node:
            arr2.append(node.val)
            node = node.next

        num1 = int(''.join(map(str, arr1[::-1])))
        num2 = int(''.join(map(str, arr2[::-1])))

        ansNum = num1 + num2
        arrAns = list(str(ansNum))[::-1]

        dummy = ListNode()
        curr = dummy

        for digit in arrAns:
            curr.next = ListNode(int(digit))
            curr = curr.next

        return dummy.next
