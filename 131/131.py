class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        palindrome = [[False] * len(s) for _ in s]
        for end in range(len(s)):
            for start in range(end + 1):
                if (s[start] == s[end]) and (end - start <= 2 or palindrome[start + 1][end - 1]):
                    palindrome[start][end] = True

        out = []
        stack = [([], 0)]
        while stack:
            result, start = stack.pop()
            if start == len(s):
                out.append(result)
            else:
                for i in range(start, len(s)):
                    if palindrome[start][i]:
                        stack.append((result + [s[start: i + 1]], i + 1))
        return out
            
            
#         new_s = "^"
#         for c in s:
#             new_s += "#" + c
#         new_s += "#$"
        
#         radi = [0] * len(new_s)
#         max_r_idx = 1
#         center = 0
#         right_side = 0
        
#         for i in range(1, len(new_s) - 1):
#             if i < right_side:
#                 i_mirror = 2 * center - i
#                 radi[i] = min(right_side - i, radi[i_mirror])
            
#             while(new_s[i + radi[i] + 1] == new_s[i - radi[i] - 1]):
#                 radi[i] += 1
                
#             if i + radi[i] > right_side:
#                 center = i
#                 right_side = i + radi[i]
                
#             if radi[i] > radi[max_r_idx]:
#                 max_r_idx = i
        
#         out = []
#         max_r = radi[max_r_idx]
#         # print(new_s[:-1])
#         # print(radi)
#         rs = list(set(radi))[1:]
#         for r in rs:
        
#             palindrome_r = []
#             most_right = 0
#             local_radi = [ra for ra in radi]
#             for i, ra in enumerate(radi):
#                 local_r = min(r, ra)
#                 local_radi[i - local_r : i + local_r + 1] = [local_r] * (2 * local_r + 1)
#             #     print(radi)
#             #     print(local_radi)
#             #     print("----------")
#             # print(radi)
#             # print(local_radi)
#             for i in range(1, len(new_s) - 1):
#                 if i <= most_right or local_radi[i] == 0:
#                     continue
#                 local_r = min(r, local_radi[i])
#                 palindrome_r.append(s[(i - 1)//2: (i - 1)//2 + local_r])
#                 # palindrome_r.append((local_r, s[(i - radi[i])//2: (i - radi[i])//2 + local_r]))
#                 most_right += local_r * 2
#             out.append(palindrome_r)
            
#         return out