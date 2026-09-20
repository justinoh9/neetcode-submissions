class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        at the very core, the problem entails receiving a list filled with integers, an integer k
        and returning a list of integers with k length of the most frequent integers in the nums arr

        when dealing with freq, it is ideal to use a dict or hashmap

        but also when dealing with a hashmap, it is difficult to sort the values alone

        thats why we use a sort of bucket sort approach
        putting the frequencies in a list, and then sorting that list

        this approach can also deal with elements having the same frequencies
        '''

        # first we should populate a hashmap with values and their respective frequencies

        valFreq = {}

        for i, val in enumerate(nums):
            valFreq[val] = valFreq.get(val, 0) + 1

        count = [ [] for i in range(len(nums) + 1) ]

        # now populate count by iterating through dict

        for val, freq in valFreq.items():
            count[freq].append(val)

        res = []

        # from now on, since we populated count, we can work from there. dict is done

        # since we want the most frequent k elements, and count is filled from least freq to most freq
        # iterate through count backwards

        for i in range(len(count) - 1, 0, -1): # from end of list to beginning of list

            # now we have index of count backwards
            # since count is a list of lists, we need to enter each sublist and iterate through it
            for num in count[i]:
                res.append(num)
                if len(res) == k:
                    return res
        return res

            