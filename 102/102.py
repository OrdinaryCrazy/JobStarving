# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        level_current = 0
        level = [root]
        next_level = []
        
        out_list = []
        level_list = []
        while level_current < len(level):
            node = level[level_current]
            level_current += 1
            
            level_list.append(node.val)
            if node.left is not None:
                next_level.append(node.left)
            if node.right is not None:
                next_level.append(node.right)
            
            if level_current == len(level):
                out_list.append(level_list)
                level_current = 0
                level = next_level
                next_level = []
                level_list = []
        
        return out_list
            
        
        