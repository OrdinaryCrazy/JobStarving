class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        if not s:
            return []
        stack = [(0, "", "")]
        output = []
        length = len(s)
        while stack:
            start_index, cur_string, cur_done = stack.pop()
            if start_index == length:
                if cur_string == "":
                    output.append(cur_done.strip())
            else:
                if cur_string + s[start_index] in wordDict:
                    stack.append((start_index + 1, "", cur_done + cur_string + s[start_index] + " "))
                stack.append((start_index + 1, cur_string + s[start_index], cur_done))
        return output