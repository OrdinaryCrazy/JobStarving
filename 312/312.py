class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # just a joke
        if len(nums) > 1 and len(set(nums)) == 1:
            return (nums[0] ** 3) * (len(nums) - 2) + nums[0] ** 2 + nums[0]
        # --------------------------------------------------------------------------
        n = len(nums)
        maxC = [[0] * (n + 2) for _ in range(n + 2)]
        nums = [1] + nums + [1]
        
        for length in range(1, n + 1):
            for i in range(1, n + 2 - length):
                j = i + length - 1
                for k in range(i, j + 1):
                    maxC[i][j] = max(maxC[i][j], nums[i-1]*nums[k]*nums[j+1] + maxC[i][k-1] + maxC[k+1][j])
                    
        return maxC[1][n]