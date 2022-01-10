# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        cur_level = [root]
        nex_level = []
        out = []
        while cur_level:
            local_out = [node.val for node in cur_level]
            for node in cur_level:
                if node.left:
                    nex_level.append(node.left)
                if node.right:
                    nex_level.append(node.right)
            cur_level = nex_level
            nex_level = []
            out.append(local_out)
        return out[::-1]