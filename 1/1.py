class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_num = [[i, num] for i, num in enumerate(nums)]
        index_num.sort(key=lambda x:x[1])
        left = 0
        right = len(nums) - 1
        while right > left:
            cur_sum = index_num[left][1] + index_num[right][1]
            if cur_sum == target:
                return [index_num[left][0], index_num[right][0]]
            if cur_sum > target:
                right -= 1
            else:
                left += 1