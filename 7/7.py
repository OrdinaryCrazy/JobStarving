class Solution:
    def reverse(self, x: int) -> int:
        sign = (x > 0) - (x < 0)
        x = int(str(x * sign)[::-1]) * sign
        return x if x <= 2**31 - 1 and x > -2**31 else 0