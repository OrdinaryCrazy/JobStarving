class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        divide = [True] + [False] * len(s)
        for i in range(len(s) + 1):
            for word in wordDict:
                if i >= len(word) and divide[i - len(word)] and s[i - len(word): i] == word:
                    divide[i] = True
                    break
        return divide[-1]