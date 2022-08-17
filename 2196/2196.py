# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        graph = {}
        in_degree = {}
        for des in descriptions:
            # if des[0] not in graph:
            #     graph[des[0]] = [None, None]
            # if des[1] not in graph:
            #     graph[des[1]] = [None, None]
            # graph[des[0]][des[2]] = des[1]
            if des[0] not in graph:
                graph[des[0]] = 0
            if des[1] not in graph:
                graph[des[1]] = 0
            in_degree[des[1]] = 1
        root = list(set(graph.keys()) - set(in_degree.keys()))[0]
        
        nodes = {}
        for key in graph:
            nodes[key] = TreeNode(key)

        for des in descriptions:
            if des[2] == 0:
                nodes[des[0]].right = nodes[des[1]]
            else:
                nodes[des[0]].left = nodes[des[1]]
        
        return nodes[root]