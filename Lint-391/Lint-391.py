"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param airplanes: An interval array
    @return: Count of airplanes are in the sky.
    """
    def countOfAirplanes(self, airplanes):
        # write your code here
        queue = []
        for plane in airplanes:
            queue.append((plane.start, 1))
            queue.append((plane.end, 0))
        queue.sort(key=lambda x:x)
        cnt = 0
        max_cnt = 0
        for time, event in queue:
            if event == 1:
                cnt += 1
                if cnt > max_cnt:
                    max_cnt = cnt
            else:
                cnt -= 1
        return max_cnt