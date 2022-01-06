class Trie:

    def __init__(self):
        self.firstChar = [{}, False]

    def insert(self, word: str) -> None:
        curChar = self.firstChar[0]
        # for i, char in enumerate(word):
        #     if char in curChar.keys():
        #         curChar[char][1] = (i + 1 == len(word)) or curChar[char][1]
        #         curChar = curChar[char][0]
        #     else:
        #         curChar[char] = [{}, i + 1 == len(word)]
        #         curChar = curChar[char][0]
        for i, char in enumerate(word[:-1]):
            if char in curChar.keys():
                curChar = curChar[char][0]
            else:
                curChar[char] = [{}, False]
                curChar = curChar[char][0]
                
        if word[-1] in curChar.keys():
            curChar[word[-1]][1] = True
        else:
            curChar[word[-1]] = [{}, True]

    def search(self, word: str) -> bool:
        curChar = self.firstChar[0]
        for char in word[:-1]:
            if char not in curChar.keys():
                return False
            else:
                curChar = curChar[char][0]
        
        if word[-1] in curChar.keys():
            return curChar[word[-1]][1]
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        curChar = self.firstChar[0]
        for char in prefix:
            if char not in curChar.keys():
                return False
            else:
                curChar = curChar[char][0]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)