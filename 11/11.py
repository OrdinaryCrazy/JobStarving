class Solution:
    def maxArea(self, height: List[int]) -> int:
        # two-pointer sliding window
        left = 0
        right = len(height) - 1
        maxV = 0
        while left < right:
            maxV = max(maxV, (right - left) * min(height[right], height[left]))
            if height[right] > height[left]:
                left += 1
            else:
                right -= 1
        return maxV