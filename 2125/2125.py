class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        total = 0
        pre = bank[0].count("1")
        for i in range(1, len(bank)):
            cur = bank[i].count("1")
            if cur != 0:
                total += pre * cur
                pre = cur
        return total