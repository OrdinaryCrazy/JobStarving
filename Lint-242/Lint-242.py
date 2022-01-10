"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""
class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {ListNode[]} a lists of linked list
    def binaryTreeToLists(self, root):
        # Write your code here
        if not root:
            return []
        cur_level = [root]
        nex_level = []
        out = []
        while cur_level:
            head = ListNode(0)
            pre = head
            for node in cur_level:
                if node.left:
                    nex_level.append(node.left)
                if node.right:
                    nex_level.append(node.right)
                ll_node = ListNode(node.val)
                pre.next = ll_node
                pre = pre.next
            out.append(head.next)
            cur_level = nex_level
            nex_level = []
        return out