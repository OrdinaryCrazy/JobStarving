class Solution:
    def search(self, nums: List[int], target: int) -> int:
        head = 0
        tail = len(nums) - 1
        while(head <= tail):
            mid = (head + tail) // 2
            if(nums[mid] == target):
                return mid
            if(nums[mid] < nums[tail]):
                if(nums[mid] < target and nums[tail] >= target):
                    head = mid + 1
                else:
                    tail = mid - 1
            else:
                if(nums[mid] > target and nums[head] <= target):
                    tail = mid - 1
                else:
                    head = mid + 1
        return -1