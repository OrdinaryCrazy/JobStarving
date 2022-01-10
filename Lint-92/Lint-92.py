class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """
    def backPack(self, m, A):
        value = [0] * (m + 1)
        for v in A:
            for cap in range(m, v - 1, -1):
                value[cap] = max(value[cap - v] + v, value[cap])
        for v in range(m, -1, -1):
            if value[v] > 0:
                return value[v]