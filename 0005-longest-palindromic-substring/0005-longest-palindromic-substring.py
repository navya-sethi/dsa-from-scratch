class Solution:
    def expand(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    def longestPalindrome(self, s):
        ans = ""

        for i in range(len(s)):
            p1 = self.expand(s, i, i)
            p2 = self.expand(s, i, i + 1)

            if len(p1) > len(ans):
                ans = p1

            if len(p2) > len(ans):
                ans = p2

        return ans
        