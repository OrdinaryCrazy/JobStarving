class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        max_len = 1
        cur_end_s = s[0:1]
        for i in range(1, len(s)):
            if s[i] not in cur_end_s:
                cur_end_s += s[i]
                max_len = max(max_len, len(cur_end_s))
            else:
                cur_end_s = cur_end_s[cur_end_s.index(s[i]) + 1:] + s[i]
        return max_len
        #----------------------------------------------------------------------------
        # # max_len = 1
        # max_len_stop_here = [1] * len(s)
        # for i in range(1, len(s)):
        #     if s[i] not in s[i - max_len_stop_here[i - 1]: i]:
        #         max_len_stop_here[i] = max_len_stop_here[i - 1] + 1
        #         # max_len = max(max_len, max_len_stop_here[i])
        #     else:
        #         max_len_stop_here[i] = max_len_stop_here[i - 1] - s[i - max_len_stop_here[i - 1]: i].index(s[i])
        # # return max_len
        # return max(max_len_stop_here)
        #----------------------------------------------------------------------------
        # unique = list(set(s))
        # unique_num = len(unique)
        # unique_index = {c:i for i, c in enumerate(unique)}
        # unique_count = [[0] * unique_num] + [[0] * unique_num for c in s]
        # for i in range(1, len(s) + 1):
        #     unique_count[i] = [cnt for cnt in unique_count[i - 1]]
        #     unique_count[i][unique_index[s[i - 1]]] += 1
        # max_len = 1
        # for i in range(len(s) + 1):
        #     for j in range(i + 1, len(s) + 1):
        #         if sum([jl - ik > 1 for ik, jl in zip(unique_count[i], unique_count[j])]) == 0:
        #             max_len = max(j - i, max_len)
        # return max_len