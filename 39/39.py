class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        stack = [(0, [], target)]
        candidates.sort()
        num_candidate = len(candidates)
        while stack:
            start_index, cur_comb, res_target = stack.pop()
            while start_index < num_candidate and res_target > 0:
                if candidates[start_index] == res_target:
                    output.append(cur_comb + [candidates[start_index]])
                stack.append(
                    (start_index, 
                     cur_comb + [candidates[start_index]], 
                     res_target - candidates[start_index])
                )
                start_index += 1
        return output