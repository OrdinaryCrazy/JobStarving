class NumArray:

    def __init__(self, nums: List[int]):
        # Binary Index Tree
        self.size = len(nums)
        self.BITree = [0] * (self.size + 1)
        for i in range(self.size):
            self.update(i, nums[i])

    def update(self, index: int, val: int) -> None:
        # The child node BITree[x] of the node BITree[y] stores the sum of the elements 
        # between y(inclusive) and x(exclusive): arr[y,…,x). 
        val = val - self.sumRange(index, index)
        index += 1
        while index <= self.size:
            self.BITree[index] += val
            # key of BITree
            index = index + (index & (-index))

    def sumRange(self, left: int, right: int) -> int:
        sum_left = 0
        sum_right = 0
        
        right += 1
        
        while left > 0:
            sum_left += self.BITree[left]
            left = left - (left & (-left))
            
        while right > 0:
            sum_right += self.BITree[right]
            right = right - (right & (-right))
            
        return sum_right - sum_left


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)