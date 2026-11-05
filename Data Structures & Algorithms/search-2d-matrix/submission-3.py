class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        2d arr
        return a bool



        '''

        left = 0
        right = len(matrix) - 1

        while left <= right:
            mid = (left + right) // 2
            if target >= matrix[mid][0] and target <= matrix[mid][-1]:
                l, r = 0, len(matrix[mid]) - 1
                while l <= r:
                    m = (l + r) // 2
                    if target == matrix[mid][m]:
                        return True
                    elif target > matrix[mid][m]:
                        l = m + 1
                    else:
                        r = m - 1
                return False
            elif target > matrix[mid][-1]:
                left += 1
            else:
                right -= 1
        return False