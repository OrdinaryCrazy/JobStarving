class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # Non-recursive
        # stack = [([], 1)]
        # combk = []
        # while stack:
        #     cur_combk, start_idx = stack.pop()
        #     if len(cur_combk) == k:
        #         combk.append(cur_combk)
        #     elif start_idx + 1 <= n + 1:
        #         stack.append((cur_combk, start_idx + 1))
        #         stack.append((cur_combk + [start_idx], start_idx + 1))
        # return combk
        
        # recursive
        if k == 1:
            return [[i] for i in range(1, n + 1)]
        if k == n:
            return [[i for i in range(1, n + 1)]]
        return self.combine(n - 1, k) + [comb + [n] for comb in self.combine(n - 1, k - 1)]