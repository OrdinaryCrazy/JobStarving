class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        cnt = [0] * (len(nums) + 1)
        out = []
        for num in nums:
            cnt[num] += 1
        for i, c in enumerate(cnt):
            if c == 2:
                out.append(i)
        return out