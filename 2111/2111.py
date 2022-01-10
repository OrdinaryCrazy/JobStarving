import bisect
class Solution:
    def kIncreasing(self, arr: List[int], k: int) -> int:
        n = len(arr)
        kJumpLists = []
        for i in range(k):
            kJumpList = []
            for j in range(i, n, k):
                kJumpList.append(arr[j])
            kJumpLists.append(kJumpList)
        cnt = 0
        # -----------------------------------------------------------
        # Brute Force LIS
        # -----------------------------------------------------------
        # for kJumpList in kJumpLists:
        #     maxLengthEndHere = [1] * len(kJumpList)
        #     for i in range(len(kJumpList)):
        #         for j in range(i):
        #             if kJumpList[j] <= kJumpList[i]:
        #                 maxLengthEndHere[i] = max(maxLengthEndHere[i], maxLengthEndHere[j] + 1)
        #     cnt += len(kJumpList) - max(maxLengthEndHere)
        # -----------------------------------------------------------
        # Binary Search LIS
        # -----------------------------------------------------------
        # for kJumpList in kJumpLists:
        #     smallestEndingThisLength = []
        #     for num in kJumpList:
        #         head = 0
        #         tail = len(smallestEndingThisLength)
        #         while(head < tail):
        #             mid = (head + tail) // 2
        #             if smallestEndingThisLength[mid] <= num:
        #                 head = mid + 1
        #             else:
        #                 tail = mid
        #         if tail >= len(smallestEndingThisLength):
        #             smallestEndingThisLength.append(num)
        #         else:
        #             smallestEndingThisLength[tail] = num
        #     cnt += len(kJumpList) - len(smallestEndingThisLength)
        # -----------------------------------------------------------
        # Binary Search LIS Lib
        # -----------------------------------------------------------
        for kJumpList in kJumpLists:
            smallestEndingThisLength = []
            for num in kJumpList:
                idx = bisect.bisect(smallestEndingThisLength, num)
                if idx == len(smallestEndingThisLength):
                    smallestEndingThisLength.append(num)
                else:
                    smallestEndingThisLength[idx] = num
            cnt += len(kJumpList) - len(smallestEndingThisLength)
        return cnt