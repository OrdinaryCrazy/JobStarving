# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = [root]
        next_queue = []
        result = []
        while queue:
            for node in queue:
                if node.left is not None:
                    next_queue.append(node.left)
                if node.right is not None:
                    next_queue.append(node.right)
            result.append(queue[-1].val)
            queue = next_queue
            next_queue = []
        return result
        