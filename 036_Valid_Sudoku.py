class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # Check each row
        for row in range(9):
            marker = [0] * 9
            for col in range(9):
                cur = board[row][col]
                if cur != '.':
                    cur = ord(cur) - ord('1') 
                    if marker[cur] == 0:
                        marker[cur] = 1
                    else:
                        return False

        # Check each column
        for col in range(9):
            marker = [0] * 9
            for row in range(9):
                cur = board[row][col]
                if cur != '.':
                    cur = ord(cur) - ord('1')
                    if marker[cur] == 0:
                        marker[cur] = 1
                    else:
                        return False

        # Check each square
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                marker = [0] * 9
                for j in range(3):
                    for i in range(3):
                        cur = board[row + i][col + j]
                        if cur != '.':
                            cur = ord(cur) - ord('1')
                            if marker[cur] == 0:
                                marker[cur] = 1
                            else:
                                return False
        return True
# Time: O(n2)
# Space: O(n)
