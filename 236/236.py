# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # non-recursive dfs
        stack = []
        cur = [root, root.val == p.val, root.val == q.val]
        while stack or cur[0]:
            while cur[0]:
                stack.append(cur)
                if cur[0].left is not None:
                    cur = [cur[0].left, cur[0].left.val == p.val, cur[0].left.val == q.val]
                elif cur[0].right is not None:
                    cur = [cur[0].right, cur[0].right.val == p.val, cur[0].right.val == q.val]
                else:
                    cur = [None, None, None]
                # print(len(stack), stack[-1][0].val, stack[-1][1], stack[-1][2])
        
            cur = stack.pop()
            # print(len(stack), stack[-1][0].val, cur[0] == stack[-1][0].left)
            if cur[1] and cur [2]:
                return cur[0]
            if stack:
                stack[-1][1] = stack[-1][1] or cur[1]
                stack[-1][2] = stack[-1][2] or cur[2]
                if cur[0] == stack[-1][0].left and stack[-1][0].right:
                    cur = [stack[-1][0].right, 
                           stack[-1][0].right.val == p.val, 
                           stack[-1][0].right.val == q.val]
                else:
                    cur = [None, None, None]
            else:
                cur = [None, None, None]
            
        return None
        