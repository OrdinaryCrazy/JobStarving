"""
class DirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []
"""

class Solution:
    """
    @param graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        # 0 for white
        # 1 for grey
        # 2 for black
        self.graph = graph
        self.color = [0 for node in graph]
        self.top = [0 for node in graph]
        self.top_pointer = len(graph) - 1
        # self.top_pointer = 0
        # make reverse graph
        # graph_r = [DirectedGraphNode(node.label) for node in graph]
        # for node in graph:
        #     for neigh in node.neighbors:
        #         graph_r[neigh].neighbors.append(node.label)
        # find a 0-deg node in grpah_r
        for node in self.graph:
            if self.color[node.label] == 0:
                self.DFS(node)
        return self.top

    def DFS(self, node):
        self.color[node.label] = 1
        for neigh in node.neighbors:
            if self.color[neigh.label] == 0:
                self.DFS(neigh)
        self.color[node.label] = 2
        self.top[self.top_pointer] = node
        self.top_pointer = self.top_pointer - 1
        # self.top_pointer = self.top_pointer + 1
