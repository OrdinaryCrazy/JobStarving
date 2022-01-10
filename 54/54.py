class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])
        visited = [[True] * (cols + 2)] + [[True] + [False] * cols + [True] for _ in range(rows)] + [[True] * (cols + 2)]
        out = []
        i = 1
        j = 1
        while True:
            out.append(matrix[i - 1][j - 1])
            visited[i][j] = True
            # print(out, visited)
            while not visited[i][j + 1]:
                j += 1
                out.append(matrix[i - 1][j - 1])
                visited[i][j] = True
            while not visited[i + 1][j]:
                i += 1
                out.append(matrix[i - 1][j - 1])
                visited[i][j] = True
            while not visited[i][j - 1]:
                j -= 1
                out.append(matrix[i - 1][j - 1])
                visited[i][j] = True
            while not visited[i - 1][j]:
                i -= 1
                out.append(matrix[i - 1][j - 1])
                visited[i][j] = True
                
            if not visited[i][j + 1]:
                j += 1
                continue
            else:
                return out
                