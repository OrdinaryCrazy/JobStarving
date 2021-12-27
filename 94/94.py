# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        stack = [0] * 101
        pointer = -1
        current_node = root
        out_list = []
        while(pointer >= 0 or current_node is not None):
            while(current_node is not None):
                pointer = pointer + 1
                stack[pointer] = current_node
                current_node = current_node.left
            if(pointer >= 0):
                current_node = stack[pointer]
                pointer = pointer - 1
                out_list.append(current_node.val)
                current_node = current_node.right
        return out_list