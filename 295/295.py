# import heapq
# class MedianFinder:
#     def __init__(self):
#         self.max_heap = []
#         self.min_heap = []
#     def addNum(self, num: int) -> None:
#         heapq.heappush(self.min_heap, num)
#         heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
#         if len(self.min_heap) < len(self.max_heap):
#             heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
#     def findMedian(self) -> float:
#         if len(self.min_heap) == len(self.max_heap):
#             return (self.min_heap[0] - self.max_heap[0]) / 2.0
#         else:
#             return self.min_heap[0]
            
class MedianFinder:

    def __init__(self):
        # size(min_heap) = size(max_heap) or size(max_heap) + 1
        self.max_heap = MaxPriorityQueue()
        self.min_heap = MaxPriorityQueue()

    def addNum(self, num: int) -> None:
        self.min_heap.push(num)
        self.max_heap.push(-self.min_heap.pop())
        if self.min_heap.size() < self.max_heap.size():
            self.min_heap.push(-self.max_heap.pop())

    def findMedian(self) -> float:
        if self.min_heap.size() == self.max_heap.size():
            return (self.min_heap.getMax() - self.max_heap.getMax()) / 2.0
        else:
            return self.min_heap.getMax()
        
class MaxPriorityQueue:
    
    def __init__(self):
        self.queue = []
    
    def push(self, item):
        self.queue.append(item)
        self._shiftDown(0, len(self.queue) - 1)
    
    def pop(self):
        last_item = self.queue.pop()
        if self.queue:
            out_item = self.queue[0]
            self.queue[0] = last_item
            self._shiftUp(0)
            return out_item
        return last_item
    
    def size(self):
        return len(self.queue)
    
    def getMax(self):
        return self.queue[0]
    
    def _shiftDown(self, start_pos, pos):
        new_item = self.queue[pos]
        while pos > start_pos :
            parent_pos = (pos - 1) >> 1
            parent = self.queue[parent_pos]
            if new_item > parent:
                self.queue[pos] = parent
                pos = parent_pos
            else:
                break
        self.queue[pos] = new_item
    
    def _shiftUp(self, pos):
        end_pos = self.size()
        start_pos = pos
        new_item = self.queue[pos]
        child_pos = 2 * pos + 1
        while child_pos < end_pos:
            right_pos = child_pos + 1
            if right_pos < end_pos and self.queue[right_pos] > self.queue[child_pos]:
                child_pos = right_pos
            self.queue[pos] = self.queue[child_pos]
            pos = child_pos
            child_pos = 2 * pos + 1
        self.queue[pos] = new_item
        self._shiftDown(start_pos, pos)

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()