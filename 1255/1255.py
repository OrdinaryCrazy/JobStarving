class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        cnt = [0] * 26
        for c in letters:
            cnt[ord(c) - ord("a")] += 1
        
        return self.dfs(words, cnt, score, 0)
    
    def dfs(self, words, cnt, score, start):
        result = 0
        for i in range(start, len(words)):
            max_sum_from_here = 0
            can_be_include = True
            
            for c in words[i]:
                if cnt[ord(c) - ord("a")] <= 0:
                    can_be_include = False
                cnt[ord(c) - ord("a")] -= 1
                max_sum_from_here += score[ord(c) - ord("a")]
                
            if can_be_include:
                max_sum_from_here += self.dfs(words, cnt, score, i + 1)
                result = max(result, max_sum_from_here)
                
            for c in words[i]:
                cnt[ord(c) - ord("a")] += 1
            
        return result