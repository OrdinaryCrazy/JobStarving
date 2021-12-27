class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 0 for white
        # 1 for grey
        # 2 for black

        m = len(grid)
        n = len(grid[0])
        color = [[0] * (n + 2)]
        for row in grid:
            color.append([0] + [int(col) for col in row] + [0])
        color.append([0] * (n + 2))
        num_island = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if color[i][j] == 1:
                    queue = [(i, j)]
                    color[i][j] = 2
                    queue_pointer = 0
                    while queue_pointer < len(queue):
                        k, l = queue[queue_pointer]
                        if color[k + 1][l] == 1:
                            queue.append((k + 1, l))
                            color[k + 1][l] = 2
                        if color[k][l + 1] == 1:
                            queue.append((k, l + 1))
                            color[k][l + 1] = 2
                        if color[k - 1][l] == 1:
                            queue.append((k - 1, l))
                            color[k - 1][l] = 2
                        if color[k][l - 1] == 1:
                            queue.append((k, l - 1))
                            color[k][l - 1] = 2
                        queue_pointer = queue_pointer + 1
                    num_island = num_island + 1  
        return num_island
        
        