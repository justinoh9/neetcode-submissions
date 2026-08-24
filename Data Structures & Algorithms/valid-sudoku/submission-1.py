class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # rows have no dup
        # for i in range(10):
        #     seen = {}
        #     for j in range(10):
        #         if board[i][j] not in seen and board[i][j] != ".":
        #             seen[i] = board[i][j]
        #         else:
        #             return False
        # return True
        for row in range(9):
            seen = set()
            for i in range(9):
                if board[row][i] == ".":
                    continue
                if board[row][i] in seen:
                    return False
                seen.add(board[row][i])

        for column in range(9):
            seen = set()
            for i in range(9):
                if board[i][column] == ".":
                    continue
                if board[i][column] in seen:
                    return False
                seen.add(board[i][column])
        
        for square in range(9): # basically iterating through each of the 9 squares
            seen = set() # set to check freq
            for i in range(3): # used for the mini row
                for j in range(3): # used for mini column
                    '''
                    if square is 1, checking first square
                    so it would be 0 * 3 + i
                    so basically just 0-2
                    but if it was square 4, it would be 1 * 3 + i so that would be 3-5
                    '''
                    row = (square // 3) * 3 + i 
                    
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        

        return True