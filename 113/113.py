# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        stack = [(root, [], targetSum)]
        output = []
        while stack:
            start_node, cur_path, res_target = stack.pop()
            if not start_node.left and not start_node.right and res_target == start_node.val:
                output.append(cur_path + [start_node.val])
            if start_node.left:
                stack.append((start_node.left, cur_path + [start_node.val], res_target - start_node.val))
            if start_node.right:
                stack.append((start_node.right, cur_path + [start_node.val], res_target - start_node.val))
        return output