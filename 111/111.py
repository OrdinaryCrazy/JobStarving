# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = [root]
        next_queue = []
        queue_pointer = 0
        level = 1
        cur = root
        while queue_pointer < len(queue):
            cur = queue[queue_pointer]
            queue_pointer = queue_pointer + 1
            
            if cur.left is None and cur.right is None:
                break
                
            if cur.left is not None:
                next_queue.append(cur.left)
            if cur.right is not None:
                next_queue.append(cur.right)  

            if queue_pointer == len(queue):
                if len(next_queue) > 0:
                    queue = next_queue
                    queue_pointer = 0
                    next_queue = []
                    level += 1
                else:
                    break
        return level