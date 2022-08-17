class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        directed_graph = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses
        
        for prereq in prerequisites:
            directed_graph[prereq[1]].append(prereq[0])
            in_degree[prereq[0]] += 1
        
        order = []
        zero_degree = []
        for i in range(numCourses):
            if in_degree[i] == 0:
                zero_degree.append(i)
        
        while zero_degree:
            i = zero_degree.pop()
            order.append(i)
            for j in directed_graph[i]:
                in_degree[j] -= 1
                if in_degree[j] == 0:
                    zero_degree.append(j)
        return [] if sum(in_degree) != 0 else order