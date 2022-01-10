class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        num_rows = len(s) + 1
        num_cols = len(p) + 1
        match = [[False] * num_cols for _ in range(num_rows)]
        # first col
        match[0][0] = True
        # first row
        for i in range(2, num_cols):
            if p[i - 1] == "*":
                match[0][i] = match[0][i - 2]
                
        for i in range(1, num_rows):
            for j in range(1, num_cols):
                if s[i - 1] == p[j - 1] or p[j - 1] == ".":
                    match[i][j] = match[i - 1][j - 1]
                elif p[j - 1] == "*":
                    match[i][j] = match[i][j - 2]
                    if s[i - 1] == p[j - 2] or p[j - 2] == ".":
                        match[i][j] = match[i][j - 2] or match[i - 1][j]
        return match[num_rows - 1][num_cols - 1]
                    