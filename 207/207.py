class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        directed_graph = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses
        
        for prereq in prerequisites:
            directed_graph[prereq[1]].append(prereq[0])
            in_degree[prereq[0]] += 1
        
        zero_degree = []
        for i in range(numCourses):
            if in_degree[i] == 0:
                zero_degree.append(i)
                
        while zero_degree:
            i = zero_degree.pop()
            for j in directed_graph[i]:
                in_degree[j] -= 1
                if in_degree[j] == 0:
                    zero_degree.append(j)
        
        return sum([d > 0 for d in in_degree]) == 0
# ------------------------------------------------------------------------
#         whoismypre = [set() for _ in range(numCourses)]
#         iamwhospre = [set() for _ in range(numCourses)]
        
#         for prereq in prerequisites:
#             whoismypre[prereq[0]].add(prereq[1])
#             iamwhospre[prereq[1]].add(prereq[0])
        
#         avi = set()
#         for i, prereq in enumerate(whoismypre):
#             if not prereq:
#                 avi.add(i)
#         if not avi:
#             return False
        
#         while True:
#             old_size = len(avi)
#             for i in range(numCourses):
#                 if i not in avi:
#                     if whoismypre[i].issubset(avi):
#                         avi.add(i)
#             if len(avi) == old_size:
#                 break
                    
#         return len(avi) == numCourses
            