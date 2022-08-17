class Solution:
    def uniqueLetterString(self, s: str) -> int:
        result = 0
        last = [-1] * 26
        sec_last = [-1] * 26
        
        for i in range(len(s)): 
            idx = ord(s[i]) - 65
            result += (i - last[idx]) * (last[idx] - sec_last[idx])
            sec_last[idx] = last[idx]
            last[idx] = i
        
        n = len(s)
        for i in range(26):
            result += (n - last[i]) * (last[i] - sec_last[i])
        return result
# ------------------------------------------------------------------------------------
#         sum_ending_here = [0] * (len(s) + 1)
#         last = [0] * 26
#         sec_last = [0] * 26
#         s = "#" + s
        
#         for i in range(1, len(s)):
#             idx = ord(s[i]) - 65
#             sum_ending_here[i] += sum_ending_here[i - 1] + (i - last[idx])
#             sum_ending_here[i] -= last[idx] - sec_last[idx]
#             sec_last[idx] = last[idx]
#             last[idx] = i
        
#         return sum(sum_ending_here)
        