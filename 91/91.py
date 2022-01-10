class Solution:
    def numDecodings(self, s: str) -> int:
        ways = [1] + [0] * len(s)
        if s[0] != "0":
            ways[1] = 1
            
        for i in range(2, len(s) + 1):
            if s[i - 1] == "0":
                if s[i - 2] == "1" or s[i - 2] == "2":
                    ways[i] = ways[i - 2]
                else:
                    return 0
            else:
                if s[i - 2] != "0" and s[i-2: i] <= "26":
                    ways[i] = ways[i - 2] + ways[i - 1]
                else:
                    ways[i] = ways[i - 1]
                
        return ways[-1]
        