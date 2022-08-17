class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        
        stretchy = 0
        n_s = len(s)
        
        for word in words:
            s_pointer = 0
            word_pointer = 0
            n_word = len(word)
            
            while(s_pointer < n_s):
                if word_pointer < n_word and s[s_pointer] == word[word_pointer]:
                    word_pointer += 1
                    s_pointer += 1
                elif s_pointer > 0 and s[s_pointer - 1] == s[s_pointer] and s_pointer < n_s - 1 and s[s_pointer + 1] == s[s_pointer]:
                    s_pointer += 2
                elif not (s_pointer> 1 and s[s_pointer - 1] == s[s_pointer] and s[s_pointer - 2] == s[s_pointer]):
                    break
                else:
                    s_pointer += 1
            
            if s_pointer == n_s and word_pointer == n_word:
                stretchy += 1
            
        return stretchy
        
        
        