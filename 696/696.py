class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        idx = 0
        n = len(s)
        num_mid = 0
        while idx < n - 1:
            if s[idx] != s[idx + 1]: # mid point
                r = 1
                while idx - r >= 0 and idx + r + 1 < n and s[idx - r] == s[idx] and s[idx + 1] == s[idx + r + 1]:
                    r += 1
                    # print(idx, s[idx], r)
                idx += r
                num_mid += r
            else:
                idx += 1
        return num_mid
                