class Solution:
    def numTilings(self, n: int) -> int:
        # refer: https://www.cnblogs.com/grandyang/p/9179556.html
        out = [0] *  (n + 4)
        out[0], out[1], out[2] = 1, 1, 2
        for i in range(3, n + 1):
            out[i] = int((2 * out[i - 1] + out[i - 3]) % (1e9 + 7))
        return out[n]