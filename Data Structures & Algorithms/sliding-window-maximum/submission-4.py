from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()  # Store indices
        res = []

        for i in range(len(nums)):

            # Remove indices outside the window
            if q and q[0] <= i - k:
                q.popleft()

            # Remove smaller values from the back
            while q and nums[q[-1]] <= nums[i]:
                q.pop()

            q.append(i)

            # Record max once window has k elements
            if i >= k - 1:
                res.append(nums[q[0]])

        return res