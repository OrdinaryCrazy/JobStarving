class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # -----------------------------------------------
        # curr, furthest, goal = 0,0,len(nums)-1
        # while curr <= furthest and furthest < goal:
        #     furthest = max(furthest, nums[curr] + curr)
        #     curr += 1
        # return furthest >= goal
        # -----------------------------------------------
        left_most = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= left_most:
                left_most = i
        return left_most == 0
        # -----------------------------------------------
        # target = len(nums) - 1
        # approach = [False] * len(nums)
        # approach[-1] = True
        # for i in range(len(nums) - 2, -1, -1):
        #     if i + nums[i] >= target:
        #         approach[i] = True
        #     else:
        #         for j in range(nums[i], 0, -1):
        #             if approach[i + j] is True:
        #                 approach[i] = True
        #                 break
        # return approach[0]