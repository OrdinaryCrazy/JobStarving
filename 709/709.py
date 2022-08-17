class Solution:
    def toLowerCase(self, s: str) -> str:
        out = ""
        for c in s:
            out += chr(ord(c) + 32) if ord(c) - ord("a") < 0 and ord(c) >= ord("A") and ord(c) <= ord("Z") else c
        return out