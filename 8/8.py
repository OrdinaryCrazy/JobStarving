class Solution:
    def myAtoi(self, s: str) -> int:
        factor = 1
        num = 0
        s = s.strip()
        if not s:
            return 0
        
        if s[0] == "-":
            factor *= -1
            s = s[1:]
        elif s[0] == "+":
            s = s[1:]
                
        for c in s:
            if not ("0" <= c and c <= "9"):
                break
            num = num * 10 + int(c)
        num *= factor
        num = max(num, -2**31)
        num = min(num, 2**31 - 1)
        return num