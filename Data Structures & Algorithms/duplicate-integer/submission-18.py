class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''
            okay so given an int arr
            if val appears more than once
            ret true

            else return false
        '''

        intSeen = set()

        # populate the set, check for dup before adding

        for i, n in enumerate(nums):

            if n in intSeen:
                return True
            
            intSeen.add(n)
        
        return False