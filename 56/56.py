class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        out = []
        # intervals.sort( key=lambda x:(x[0], -x[1]) )
        intervals.sort( key=lambda x:x[0] )
        start, end = intervals[0][0], intervals[0][1]
        for i in range(1, len(intervals)):
            l_start, l_end = intervals[i][0], intervals[i][1]
            if l_start <= end:
                end = max(end, l_end)
            else:
                out.append([start, end])
                start, end = l_start, l_end
        out.append([start, end])
        return out