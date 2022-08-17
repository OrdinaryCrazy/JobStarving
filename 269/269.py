class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = [set() for _ in range(26)]
        in_degree = [0] * 26
        # exist = [False] * 26
        exist = set()
        for word in words:
            for c in word:
                exist.add(c)
        
        for i in range(len(words) - 1):
            if len(words[i + 1]) < len(words[i]) and words[i + 1] == words[i][:len(words[i + 1])]:
                return ""
            n = min(len(words[i]), len(words[i + 1]))
            for j in range(n):
                if words[i][j] != words[i + 1][j]:
                    if words[i + 1][j] not in graph[ord(words[i][j]) - 97]:
                        graph[ord(words[i][j]) - 97].add(words[i + 1][j])
                        in_degree[ord(words[i + 1][j]) - 97] += 1
                    break
        # for i, word in enumerate(words):
            # for j, c in enumerate(word):
                # exist[ord(c) - 97] = True
                
                # for k in range(j + 1, len(word)):
                #     if word[k] != c and word[k] not in graph[ord(c) - 97]:
                #         graph[ord(c) - 97].add(word[k])
                #         in_degree[ord(word[k]) - 97] += 1
                
                # for k in range(i + 1, len(words)):
                #     if len(words[k]) > j:
                #         if words[k][:j] == word[:j] and words[k][j] != word[j]:
                #             if words[k][j] not in graph[ord(word[j]) - 97]:
                #                 graph[ord(word[j]) - 97].add(words[k][j])
                #                 in_degree[ord(words[k][j]) - 97] += 1
                #     else:
                #         if words[k] == word[:len(words[k])]:
                #             return ""
                #         else:
                #             break

        out = ""
        # while in_degree.count(0) > 0:
        #     idx = in_degree.index(0)
        #     for c in graph[idx]:
        #         in_degree[ord(c) - 97] -= 1
        #     in_degree[idx] = -1
        #     if exist[idx]:
        #         out += chr(idx + 97)
        # if len(out) != sum(exist):
        #     return ""
        stack = []
        for c in exist:
            if in_degree[ord(c) - 97] == 0:
                stack.append(c)
        while stack:
            c = stack.pop()
            out += c
            for neigh in graph[ord(c) - 97]:
                in_degree[ord(neigh) - 97] -= 1
                if in_degree[ord(neigh) - 97] == 0:
                    stack.append(neigh)
        if len(out) != len(exist):
            return ""
        return out
                
        