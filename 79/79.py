class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        mark = [[False] * n for _ in range(m)]
        
        def search(board, word, mark, i, j, k, m, n) -> bool:
            if k == len(word) - 1 and board[i][j] == word[k]:
                return True
            if board[i][j] == word[k]:
                mark[i][j] = True
                if i - 1 >= 0 and not mark[i - 1][j] and search(board, word, mark, i - 1, j, k + 1, m, n):
                    return True
                if i + 1 < m and not mark[i + 1][j] and search(board, word, mark, i + 1, j, k + 1, m, n):
                    return True
                if j - 1 >= 0 and not mark[i][j - 1] and search(board, word, mark, i, j - 1, k + 1, m, n):
                    return True
                if j + 1 < n and not mark[i][j + 1] and search(board, word, mark, i, j + 1, k + 1, m, n):
                    return True
                mark[i][j] = False
            return False
        
        for i in range(m):
            for j in range(n):
                if search(board, word, mark, i, j, 0, m, n):
                    return True
        return False