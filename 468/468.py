class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if len(queryIP.split(".")) == 4:
            IPitems = queryIP.split(".")
            for item in IPitems:
                if not item.isdigit():
                    return "Neither"
                elif int(item) > 255 or int(item) < 0:
                    return "Neither"
                elif len(item) > 1 and item[0] == "0":
                    return "Neither"
                else:
                    continue
            return "IPv4"
        elif len(queryIP.split(":")) == 8:
            IPitems = queryIP.split(":")
            for item in IPitems:
                if len(item) > 4 or len(item) < 1:
                    return "Neither"
                for char in item:
                    digital = char.isdigit()
                    alpha = char.isalpha()
                    alphaAF = (ord(char) >= ord("A") and ord(char) <= ord("F"))
                    alphaaf = (ord(char) >= ord("a") and ord(char) <= ord("f"))
                    if digital or (alpha and (alphaAF or alphaaf)):
                        continue
                    else:
                        return "Neither"
            return "IPv6"
                    
        else:
            return "Neither"