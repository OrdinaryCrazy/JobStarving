class Solution:
    def originalDigits(self, s: str) -> str:
        cnt = [0] * 26
        num = [0] * 10
        num_c = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        for c in s:
            cnt[ord(c) - 97] += 1
        # 0
        num[0] = cnt[ord("z") - 97]
        cnt[ord("e") - 97] -= num[0]
        # cnt[ord("r") - 97] -= num[0]
        cnt[ord("o") - 97] -= num[0]
        # 8
        num[8] = cnt[ord("g") - 97]
        cnt[ord("e") - 97] -= num[8]
        # cnt[ord("i") - 97] -= num[8]
        # cnt[ord("h") - 97] -= num[8]
        cnt[ord("t") - 97] -= num[8]
        # 6
        num[6] = cnt[ord("x") - 97]
        cnt[ord("s") - 97] -= num[6]
        # cnt[ord("i") - 97] -= num[6]
        # 7
        num[7] = cnt[ord("s") - 97]
        cnt[ord("e") - 97] -= num[7] * 2
        cnt[ord("v") - 97] -= num[7]
        # cnt[ord("n") - 97] -= num[7]
        # 5
        num[5] = cnt[ord("v") - 97]
        cnt[ord("f") - 97] -= num[5]
        # cnt[ord("i") - 97] -= num[5]
        cnt[ord("e") - 97] -= num[5]
        # 4
        num[4] = cnt[ord("f") - 97]
        cnt[ord("o") - 97] -= num[4]
        # cnt[ord("u") - 97] -= num[4]
        # cnt[ord("r") - 97] -= num[4]
        # 2
        num[2] = cnt[ord("w") - 97]
        cnt[ord("t") - 97] -= num[2]
        cnt[ord("o") - 97] -= num[2]
        # 3
        num[3] = cnt[ord("t") - 97]
        # cnt[ord("h") - 97] -= num[3]
        # cnt[ord("r") - 97] -= num[3]
        cnt[ord("e") - 97] -= num[3] * 2
        # 1
        num[1] = cnt[ord("o") - 97]
        # cnt[ord("n") - 97] -= num[1]
        cnt[ord("e") - 97] -= num[1]
        # 9
        num[9] = cnt[ord("e") - 97]
        
        return ''.join([num_c[i] * num[i] for i in range(10)])