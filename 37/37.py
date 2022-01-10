class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # preprocessing
        rows_cnt = [[False] * 9 for _ in range(9)]
        cols_cnt = [[False] * 9 for _ in range(9)]
        cell_cnt = [[False] * 9 for _ in range(9)]
        for i, row in enumerate(board):
            for j, col in enumerate(row):
                if col != ".":
                    num = int(col)
                    rows_cnt[i][num - 1] = True
                    cols_cnt[j][num - 1] = True
                    cell_idx = i//3 * 3 + j // 3
                    cell_cnt[cell_idx][num - 1] = True
                    
        def solver(rows_cnt, cols_cnt, cell_cnt, board) -> bool:         
            for i in range(9):
                for j in range(9):
                    if board[i][j] == ".":
                        cell_idx = i//3 * 3 + j // 3
                        for k in range(9):
                            if not rows_cnt[i][k] and not cols_cnt[j][k] and not cell_cnt[cell_idx][k]:
                                board[i][j] = str(k + 1)
                                rows_cnt[i][k] = True
                                cols_cnt[j][k] = True
                                cell_cnt[cell_idx][k] = True
                                if solver(rows_cnt, cols_cnt, cell_cnt, board):
                                    return True
                                
                                board[i][j] = "."
                                rows_cnt[i][k] = False
                                cols_cnt[j][k] = False
                                cell_cnt[cell_idx][k] = False
                        return False
            return True   
        # recursion
        solver(rows_cnt, cols_cnt, cell_cnt, board) 
        
        
                    