# tricky
# import math
# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         return int(math.factorial(m + n - 2) / math.factorial(m - 1) / math.factorial(n - 1))

# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         paths = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]
#         for i in range(1, m):
#             for j in range(1, n):
#                 paths[i][j] = paths[i - 1][j] + paths[i][j - 1]
#         return paths[m - 1][n - 1]

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if n > m:
            m, n = n, m
        
        paths = [1] * n
        pre = [p for p in paths]
        for i in range(1, m):
            for j in range(1, n):
                paths[j] = pre[j] + paths[j - 1]
            pre = [p for p in paths]
            
        return paths[-1]

