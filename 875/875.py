class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        
        def time(piles: List[int], k:int):
            return sum([ pile // k + (1 if pile % k > 0 else 0) for pile in piles])
        
        head = 1
        tail = max(piles)
        mid = (head + tail) // 2
        last_mid = 1
        while head <= tail:
            last_mid = mid
            mid = (head + tail) // 2
            t = time(piles, mid)
            # print(head, tail, mid, t)

            # if t == h:
            #     return mid
            # else:
            #     if t > h:
            #         head = mid + 1
            #     else:
            #         tail = mid - 1
                    
            if t > h:
                head = mid + 1
            else:
                tail = mid - 1
                    
        return head if t > h else mid