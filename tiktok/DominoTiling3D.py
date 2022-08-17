class Solution:
    def numTiling(n:int) -> int:
        fromBaseSum = [0] * (n + 3)
        out = [0] * (n + 3)
        out[0] = 1
        out[1] = 2
        out[2] = 9
        fromBaseSum[3] = 1
        for i in range(3, n + 1):
            out[i] = int( (2 * out[i - 1] + 5 * out[i - 2] + 4 * fromBaseSum[i]) % (1e9 + 7))
            fromBaseSum[i + 1] = int( (fromBaseSum[i] + out[i - 2]) % (1e9 + 7))
        return out[n]

if __name__ == "__main__":
    print("hello")
    for i in range(1, 10):
        print(Solution.numTiling(i))