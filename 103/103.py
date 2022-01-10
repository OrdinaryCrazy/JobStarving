# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        cur_level = [root]
        next_level = []
        out = []
        reverse = 0
        while cur_level:
            local_out = [node.val for node in cur_level]
            for node in cur_level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
                # local_out.append(node.val)
            if reverse == 1:
                out.append(local_out[::-1])
            else:
                out.append(local_out)
            cur_level = next_level
            next_level = []
            reverse = reverse ^ 1
        return out
        