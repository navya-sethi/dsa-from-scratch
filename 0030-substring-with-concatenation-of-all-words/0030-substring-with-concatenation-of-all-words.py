from collections import Counter

class Solution:
    def findSubstring(self, s, words):
        if not s or not words:
            return []

        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count

        if total_len > len(s):
            return []

        required = Counter(words)
        ans = []

        # Try each possible starting offset
        for offset in range(word_len):
            left = offset
            right = offset
            current = Counter()
            count = 0

            while right + word_len <= len(s):
                word = s[right:right + word_len]
                right += word_len

                if word in required:
                    current[word] += 1
                    count += 1

                    # Too many copies of this word
                    while current[word] > required[word]:
                        left_word = s[left:left + word_len]
                        current[left_word] -= 1
                        left += word_len
                        count -= 1

                    # All words matched
                    if count == word_count:
                        ans.append(left)

                        # Move window forward
                        left_word = s[left:left + word_len]
                        current[left_word] -= 1
                        left += word_len
                        count -= 1

                else:
                    # Invalid word, restart window
                    current.clear()
                    count = 0
                    left = right

        return ans