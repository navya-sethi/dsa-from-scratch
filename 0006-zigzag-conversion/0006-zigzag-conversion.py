class Solution:
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows
        currRow = 0
        goingDown = False

        for char in s:
            rows[currRow] += char

            if currRow == 0 or currRow == numRows - 1:
                goingDown = not goingDown

            if goingDown:
                currRow += 1
            else:
                currRow -= 1

        return "".join(rows)