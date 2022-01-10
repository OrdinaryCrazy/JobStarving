class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        subsum = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            subsum[i] = max(subsum[i - 1] + nums[i - 1], nums[i - 1])
        return max(subsum[1:])