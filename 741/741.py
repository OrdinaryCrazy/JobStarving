class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        # ----------------------------------------------------------------------
        # refer: https://www.cnblogs.com/grandyang/p/8215787.html
        # https://leetcode.com/problems/cherry-pickup/discuss/109903/step-by-step-guidance-of-the-on3-time-and-on2-space-solution
        # ----------------------------------------------------------------------
        n = len(grid)
        mostGainsRound = [[0] * n for _ in range(n)]
        mostGainsRound[0][0] = grid[0][0]
        for k in range(1, 2 * n - 1):
            # Because when you calculating dp[i][p], 
            # you need the result of dp[i - 1][p] and dp[i][p - 1], and if you add back the third dimension n 
            # they are actually dp[n - 1][i - 1][p] and dp[n - 1][i][p - 1]. 
            # If you loop i and p from 0 to N, then when you calculating dp[i][p], 
            # the result of dp[i - 1][p] and dp[i][p - 1] have already been updated, 
            # they have been updated to represent dp[n][i - 1][p] and dp[n][i][p - 1]
            for i in range(n - 1, -1, -1):
                for p in range(n - 1, -1, -1):
                    j = k - i
                    q = k - p
                    if j < 0 or j >= n or q < 0 or q >= n or grid[i][j] < 0 or grid[p][q] < 0:
                        mostGainsRound[i][p] = -1
                    else:
                        # case 1: both workers from left
                        # dp[i][p] store the answer already because j is at last step "(step-1) - i"
                        
                        # case 2: worker i from top and work p from lefe
                        if i > 0 and mostGainsRound[i - 1][p] > mostGainsRound[i][p]:
                            mostGainsRound[i][p] = mostGainsRound[i - 1][p]
                        
                        # case 3: worker p from top and work i from lefe
                        if p > 0 and mostGainsRound[i][p - 1] > mostGainsRound[i][p]:
                            mostGainsRound[i][p] = mostGainsRound[i][p - 1]
                        
                        # case 4: both workers from top
                        if i > 0 and p > 0 and mostGainsRound[i - 1][p - 1] > mostGainsRound[i][p]:
                            mostGainsRound[i][p] = mostGainsRound[i - 1][p - 1]
                            
                        if mostGainsRound[i][p] >= 0:
                            mostGainsRound[i][p] += grid[i][j] + (grid[p][q] if i != p else 0)
                            
        return max(mostGainsRound[n - 1][n - 1], 0)
        # ----------------------------------------------------------------------
        # n = len(grid)
        # mostGainsUntil = [[0] * n for _ in range(n)]
        # passed = [[set()] * n for _ in range(n)]
        # passed[0][0] = {(0, 0)}
        # mostGainsUntil[0][0] = grid[0][0]
        # for i in range(n):
        #     for j in range(n):
        #         if grid[i][j] == -1:
        #             continue
        #         if i != n - 1 and grid[i + 1][j] >= 0:
        #             gain = 1 if (i + 1, j) not in passed[i][j] and grid[i + 1][j] == 1 else 0
        #             if mostGainsUntil[i][j] + gain > mostGainsUntil[i + 1][j]:
        #                 mostGainsUntil[i + 1][j] = mostGainsUntil[i][j] + gain
        #                 passed[i + 1][j] = passed[i][j].union({(i + 1, j)})
        #         if j != n - 1 and grid[i][j + 1] >= 0:
        #             gain = 1 if (i, j + 1) not in passed[i][j] and grid[i][j + 1] == 1 else 0
        #             if mostGainsUntil[i][j] + gain > mostGainsUntil[i][j + 1]:
        #                 mostGainsUntil[i][j + 1] = mostGainsUntil[i][j] + gain
        #                 passed[i][j + 1] = passed[i][j].union({(i, j + 1)})
        # # print(mostGainsUntil, passed[n - 1][n - 1])
        # for i in range(n - 1, -1, -1):
        #     for j in range(n - 1, -1, -1):
        #         if grid[i][j] == -1:
        #             continue
        #         if i != 0 and grid[i - 1][j] >= 0:
        #             gain = 1 if (i - 1, j) not in passed[i][j] and grid[i - 1][j] == 1 else 0
        #             if mostGainsUntil[i][j] + gain > mostGainsUntil[i - 1][j]:
        #                 mostGainsUntil[i - 1][j] = mostGainsUntil[i][j] + gain
        #                 passed[i - 1][j] = passed[i][j].union({(i - 1, j)})
        #         if j != 0 and grid[i][j - 1] >= 0:
        #             gain = 1 if (i, j - 1) not in passed[i][j] and grid[i][j - 1] == 1 else 0
        #             if mostGainsUntil[i][j] + gain > mostGainsUntil[i][j - 1]:
        #                 mostGainsUntil[i][j - 1] = mostGainsUntil[i][j] + gain
        #                 passed[i][j - 1] = passed[i][j].union({(i, j - 1)})
        # return mostGainsUntil[0][0] if (n - 1, n - 1) in passed[0][0] else 0