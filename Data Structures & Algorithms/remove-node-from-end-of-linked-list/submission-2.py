class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        slowPrev = None
        fast = head

        # Move fast n-1 positions ahead
        for i in range(n - 1):
            fast = fast.next

        # Move both pointers until fast reaches the end
        while fast.next:
            fast = fast.next
            slowPrev = slow
            slow = slow.next

        # Removing the head
        if slowPrev is None:
            return head.next

        # Removing any other node
        slowPrev.next = slow.next

        return head