class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # nums.sorted()
        # res = defaultdict(int)
        # for i in nums:
        #     res[i].append(i)
        # res.sorted()
        # final = []
        # for j in range(len(res)-1, -1, -1):
        #     if k != 0:
        #         final.append(res[j])

        # return final

        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        sorted_items = sorted(count.items(), key=lambda x: x[1], reverse=True)

        final = []
        for i in range(k):
            final.append(sorted_items[i][0])
        return final                