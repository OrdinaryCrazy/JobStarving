class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s
        numChar = len(s)
        # out = " " * numChar
        out = ""
        numCols = (numChar // (2 * numRows - 2)) + (numChar % (2 * numRows - 2) // numRows)
        pattern_length = (2 * numRows - 2)
        # for i in range(0, numCols, (numRows - 1)):
        # 0 line
        for i in range(0, numChar, pattern_length):
            out += s[i]
        # 1 ~ (r - 1) line
        for i in range(1, numRows - 1):
            for j in range(i, numChar, pattern_length):
                out += s[j]
                if j + (pattern_length - 2 * i) < numChar:
                    out += s[j + (pattern_length - 2 * i)]
        # r line
        for i in range(numRows - 1, numChar, pattern_length):
            out += s[i]
        
        return out 