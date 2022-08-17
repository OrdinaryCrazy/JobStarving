class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        n = len(nums)
        valid = [False] * (n + 1)
        pos = [0] * (n + 1)
        for i, num in enumerate(nums):
            pos[num] = i
        for seq in sequences:
            for i in range(len(seq) - 1):
                if pos[seq[i]] > pos[seq[i + 1]]:
                    return False
                if pos[seq[i]] + 1 == pos[seq[i + 1]]:
                    valid[seq[i]] = True
        return sum(valid) == n - 1
        # ------------------------------------------------------------
        # graph = [[] for _ in range(len(nums))]
        # in_degree = [0] * len(nums)
        # for subs in sequences:
        #     for i in range(len(subs) - 1):
        #         for j in range(i + 1, len(subs)):
        #             if subs[j] not in graph[subs[i] - 1]:
        #                 graph[subs[i] - 1].append(subs[j])
        #                 in_degree[subs[j] - 1] += 1
        # for i in nums:
        #     if in_degree[i - 1] != 0 or in_degree.count(0) > 1:
        #         return False
        #     for j in graph[i - 1]:
        #         in_degree[j - 1] -= 1
        #     in_degree[i - 1] = -1
        # return True
        