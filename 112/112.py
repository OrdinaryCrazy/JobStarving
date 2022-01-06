# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        stack = [root]
        value_stack = [0]
        cur = root
        while stack:
            cur = stack.pop()
            cur_val = value_stack.pop() + cur.val

            if cur.left is None and cur.right is None and cur_val == targetSum:
                return True
            if cur.left is not None:
                stack.append(cur.left)
                value_stack.append(cur_val)
            if cur.right is not None:
                stack.append(cur.right)
                value_stack.append(cur_val)
                
        return False