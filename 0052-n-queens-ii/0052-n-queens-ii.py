class Solution:
    def totalNQueens(self, n):
        board = [-1] * n

        def isSafe(row, col):
            for prevRow in range(row):
                prevCol = board[prevRow]

                # Same column
                if prevCol == col:
                    return False

                # Same diagonal
                if abs(prevRow - row) == abs(prevCol - col):
                    return False

            return True

        def backtrack(row):
            # All queens placed
            if row == n:
                return 1

            count = 0

            for col in range(n):

                if isSafe(row, col):

                    # Place queen
                    board[row] = col

                    # Move to next row
                    count += backtrack(row + 1)

                    # Remove queen
                    board[row] = -1

            return count

        return backtrack(0)