import random
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # ------------------------------------------------
        def merge(p:List[int], q:List[int]):
            lp, lq = len(p), len(q)
            out = [0] * (lp + lq)
            i = 0
            j = 0
            k = 0
            while i < lp and j < lq:
                if p[i] < q[j]:
                    out[k] = p[i]
                    i += 1
                    k += 1
                else:
                    out[k] = q[j]
                    j += 1
                    k += 1
            if i < len(p):
                out[k:] = p[i:]
            if j < len(q):
                out[k:] = q[j:]
            return out
        # ------------------------------------------------
        if len(nums) < 2:
            return nums
        
        lists = [[num] for num in nums]
        next_lists = []
        while len(lists) > 1:
            for i in range(0, len(lists) - 1, 2):
                next_lists.append(merge(lists[i], lists[i + 1]))
            if len(lists) % 2 > 0:
                next_lists.append(lists[-1])
            lists = next_lists
            next_lists = []
        return lists[0]
        # ------------------------------------------------
        # if len(nums) < 2:
        #     return nums
        # random.shuffle(nums)
        # pivot = nums[0]
        # i = 0
        # j = len(nums) - 1
        # while i < j:
        #     while(i < j and nums[j] > pivot):
        #         j -= 1
        #     if(i < j):
        #         nums[i] = nums[j]
        #         i += 1
        #     while(i < j and nums[i] < pivot):
        #         i += 1
        #     if(i < j):
        #         nums[j] = nums[i]
        #         j -= 1
        # nums[i] = pivot
        # nums[:i] = self.sortArray(nums[:i])
        # nums[i+1:] = self.sortArray(nums[i+1:])
        # ------------------------------------------------
        # if len(nums) < 2:
        #     return nums
        # random.shuffle(nums)
        # pivot = nums[-1]
        # i = 0
        # j = 0
        # while j < len(nums) - 1:
        #     if nums[j] < pivot:
        #         temp = nums[i]
        #         nums[i] = nums[j]
        #         nums[j] = temp
        #         i += 1
        #     j += 1
        # temp = nums[i]
        # nums[i] = nums[-1]
        # nums[-1] = temp
        # nums[:i] = self.sortArray(nums[:i])
        # nums[i+1:] = self.sortArray(nums[i+1:])
        # ------------------------------------------------
        return nums