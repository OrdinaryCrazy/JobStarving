class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # stack = [(1, nums[0], 1)]
        # max_length = 1
        # total_num = len(nums)
        # while stack:
        #     start_idx, last, length = stack.pop()
        #     if start_idx == total_num:
        #         if length > max_length:
        #             max_length = length
        #         continue
        #     if nums[start_idx] > last:
        #         stack.append((start_idx + 1, nums[start_idx], length + 1))
        #     stack.append((start_idx + 1, last, length))
        #     stack.append((start_idx + 1, nums[start_idx], 1))
        # return max_length
        
        max_length_ending_here = [1] * len(nums)
        max_length = 1
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j] and max_length_ending_here[i] < max_length_ending_here[j] + 1:
                    max_length_ending_here[i] = max_length_ending_here[j] + 1
            if max_length_ending_here[i] > max_length:
                max_length = max_length_ending_here[i]
        return max_length