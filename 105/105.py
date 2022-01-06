# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        num_node = len(preorder)
        
        if num_node == 0:
            return None
        
        visited = [0] * num_node
        stack = [0] * num_node
        stack_pointer = 0
        
        processing_pointer = 1
        current_root_idx = inorder.index(preorder[0])
        current_root_pointer = TreeNode(preorder[0])
        visited[current_root_idx] = 1
        
        root = current_root_pointer
        
        while(processing_pointer < num_node):
            # build left subtree, the first node in inorder does not have left
            if(current_root_idx > 0 and visited[current_root_idx - 1] == 0):
                current_root_pointer.left = TreeNode(preorder[processing_pointer])
                current_root_idx = inorder.index(preorder[processing_pointer])
                visited[current_root_idx] = 1
                processing_pointer = processing_pointer + 1
                
                stack[stack_pointer] = current_root_pointer
                stack_pointer = stack_pointer + 1
                
                current_root_pointer = current_root_pointer.left
            # build right subtree, the last node in inorder does not have right
            elif(current_root_idx + 1 < num_node and visited[current_root_idx + 1] == 0):
                current_root_pointer.right = TreeNode(preorder[processing_pointer])
                current_root_idx = inorder.index(preorder[processing_pointer])
                visited[current_root_idx] = 1
                processing_pointer = processing_pointer + 1
                
                stack[stack_pointer] = current_root_pointer
                stack_pointer = stack_pointer + 1
                
                current_root_pointer = current_root_pointer.right
            # finish building a subtree
            else:
                current_root_pointer = stack[stack_pointer - 1]
                stack_pointer = stack_pointer - 1
                
                current_root_idx = inorder.index(current_root_pointer.val)
                
        return root
                