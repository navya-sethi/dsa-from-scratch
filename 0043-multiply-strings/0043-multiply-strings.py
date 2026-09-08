class Solution:
    def multiply(self, num1, num2):

        if num1 == "0" or num2 == "0":
            return "0"

        result = [0] * (len(num1) + len(num2))

        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):

                n1 = ord(num1[i]) - ord('0')
                n2 = ord(num2[j]) - ord('0')

                product = n1 * n2

                pos1 = i + j
                pos2 = i + j + 1

                total = product + result[pos2]

                result[pos2] = total % 10
                result[pos1] += total // 10

        answer = ""

        for digit in result:
            answer += str(digit)

        return answer.lstrip("0")