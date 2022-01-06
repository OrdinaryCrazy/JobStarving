class Solution:
    def longestPalindrome(self, s: str) -> str:
        #---------------------------------------------------------------------
        new_s = "^"
        for c in s:
            new_s = new_s + "#" + c
        new_s = new_s + "#" + "$"
        
        Range = [0] * len(new_s)
        maxRangeIndex = 1
        center = 0
        right_side = 0
        
        for i in range(1, len(new_s) - 1):
            
            if(i < right_side):
                iMirror = 2 * center - i
                Range[i] = min(right_side - i, Range[iMirror])

            while(new_s[i + Range[i] + 1] == new_s[i - Range[i] - 1]):
                Range[i] += 1
            
            if(i + Range[i] > right_side):
                center = i
                right_side = i + Range[i]
            
            if(Range[i] > Range[maxRangeIndex]):
                maxRangeIndex = i
        
        start = (maxRangeIndex - Range[maxRangeIndex])//2
        return s[start : start + Range[maxRangeIndex]]
        #---------------------------------------------------------------------
        # length = len(s)
        # longest = s[0]
        # def findLongest(s, l, r):
        #     while l >= 0 and r < len(s) and s[l] == s[r]:
        #         r += 1
        #         l -= 1
        #     return s[l + 1 : r]
        # for i in range(length):
        #     s1 = findLongest(s, i, i)
        #     if len(s1) > len(longest):
        #         longest = s1
        #     s2 = findLongest(s, i, i + 1)
        #     if len(s2) > len(longest):
        #         longest = s2
        # return longest
        #---------------------------------------------------------------------
        # length = len(s)
        # longest = s[0]
        # palindrome = [[False] * length for _ in range(length)]
        # for start in range(length - 1, -1, -1):
        #     palindrome[start][start] = True
        #     for end in range(start + 1, length):
        #         if s[start] == s[end]:
        #             if end - start == 1 or palindrome[start + 1][end - 1]:
        #                 palindrome[start][end] = True
        #                 if end - start + 1 > len(longest):
        #                     longest = s[start : end + 1]
        # return longest
        #---------------------------------------------------------------------
        # def LCS(s1: str, s2: str) -> str:
        #     lcs = [''] * (len(s2) + 1)
        #     longest_subs = ''
        #     for i in range(len(s1)):
        #         for j in range(len(s2) - 1, -1, -1):
        #             if(s1[i] == s2[j]):
        #                 lcs[j + 1] = lcs[j] + s2[j]
        #                 if len(lcs[j + 1]) > len(longest_subs) and lcs[j + 1] == lcs[j + 1][::-1]:
        #                     longest_subs = lcs[j + 1]
        #             else:
        #                 lcs[j + 1] = ''
        #     return longest_subs
        # return LCS(s, s[::-1])
        #---------------------------------------------------------------------