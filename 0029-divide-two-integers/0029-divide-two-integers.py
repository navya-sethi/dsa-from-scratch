class Solution:
    def divide(self, dividend, divisor):
        if dividend == -2147483648 and divisor == -1:
            return 2147483647

        negative = (dividend < 0) != (divisor < 0)

        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0

        while dividend >= divisor:
            temp = divisor
            multiple = 1

            while (temp << 1) <= dividend:
                temp = temp << 1
                multiple = multiple << 1

            dividend = dividend - temp
            quotient = quotient + multiple

        if negative:
            quotient = -quotient

        return quotient