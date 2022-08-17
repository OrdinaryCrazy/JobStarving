class Solution:
    def decodeString(self, s: str) -> str:
        curString = ['']
        repeatStack = []
        i = 0
        n = len(s)
        while i < n:
            if s[i].isdigit():
                j = i + 1
                while s[j] != "[":
                    j += 1
                repeatStack.append(int(s[i:j]))
                curString.append('')
                i = j + 1
            elif s[i] == "]":
                curString[-2] += curString[-1] * repeatStack[-1]
                curString.pop()
                repeatStack.pop()
                i += 1
            else:
                while i < n and s[i].isalpha():
                    curString[-1] += s[i]
                    i += 1
            
        return curString[0]