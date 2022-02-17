import heapq
import bisect


class MedianFinder(object):
    def __init__(self):
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        num = float(num)

        if len(self.maxHeap) == 0:
            heapq.heappush(self.maxHeap, -num)

        elif len(self.minHeap) == 0:
            if num > -self.maxHeap[0]:
                heapq.heappush(self.minHeap, num)
            else:
                # heapq.heappush(self.maxHeap, -num)
                # a = -heapq.heappop(self.maxHeap)
                a = -heapq.heappushpop(self.maxHeap, -num)
                heapq.heappush(self.minHeap, a)

        elif len(self.maxHeap) == len(self.minHeap):
            if -self.maxHeap[0] < num and self.minHeap[0] <= num:
                # heapq.heappush(self.minHeap, num)
                # a = -heapq.heappop(self.minHeap)
                a = -heapq.heappushpop(self.minHeap, num)
                heapq.heappush(self.maxHeap, a)
            else:
                heapq.heappush(self.maxHeap, -num)

        else:
            if -self.maxHeap[0] < num and self.minHeap[0] <= num:
                heapq.heappush(self.minHeap, num)
            else:
                # heapq.heappush(self.maxHeap, -num)
                # a = -heapq.heappop(self.maxHeap)
                a = -heapq.heappushpop(self.maxHeap, -num)
                heapq.heappush(self.minHeap, a)

    def findMedian(self):
        """
        :rtype: float
        """
        if (len(self.maxHeap) + len(self.minHeap)) % 2 == 0:
            return (-self.maxHeap[0] + self.minHeap[0]) / 2
        else:
            return -self.maxHeap[0]


class MedianFinder_1(object):
    def __init__(self):
        self.heap = []
        # heapq.heapify(self.heap)
        self.len = 0

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        # heapq.heappush(self.heap, num)
        bisect.insort(self.heap, num)
        self.len += 1

    def findMedian(self):
        """
        :rtype: float
        """
        if self.len % 2:
            return float(self.heap[self.len // 2])
        else:
            half = self.len // 2
            return (self.heap[half] + self.heap[half - 1]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


if __name__ == "__main__":
    obj = MedianFinder()

    obj.addNum(-1)
    print(obj.findMedian())  # -1
    obj.addNum(-2)
    print(obj.findMedian())  # -1.5
    obj.addNum(-3)
    print(obj.findMedian())  # -2
    obj.addNum(-4)
    print(obj.findMedian())  # -2.5
    obj.addNum(-5)
    print(obj.findMedian())  # -3
