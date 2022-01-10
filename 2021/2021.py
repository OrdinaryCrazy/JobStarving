class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        light_event = []
        for light in lights:
            light_event.append((light[0] - light[1], 0))
            light_event.append((light[0] + light[1], 1))
        light_event.sort(key=lambda x:x)
        max_cnt = 0
        max_pos = None
        cur_cnt = 0
        for event in light_event:
            pos, event_type = event
            if event_type == 0:
                cur_cnt += 1
            else:
                cur_cnt -= 1
            if(max_cnt < cur_cnt):
                max_pos = pos
                max_cnt = cur_cnt
        return max_pos