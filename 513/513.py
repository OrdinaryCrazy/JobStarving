# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        cur_level = [root]
        nex_level = []
        if root.left:
            nex_level.append(root.left)
        if root.right:
            nex_level.append(root.right)
        while nex_level:
            cur_level = nex_level
            nex_level = []
            for node in cur_level:
                if node.left:
                    nex_level.append(node.left)
                if node.right:
                    nex_level.append(node.right)
        return cur_level[0].val