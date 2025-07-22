import heapq

class FindMedianFromDataStream295:
    """
    Maintains a data stream and supports finding the median efficiently.

    This class uses a max-heap for the lower half of numbers and a min-heap
    for the upper half, keeping the heaps balanced to allow O(log n) insertion
    and O(1) median retrieval.

    TC: O(log n) for addNum, O(1) for findMedian.
    SC: O(n) for storing the numbers in heaps.
    """
    def __init__(self):
        self.max_heap = []
        self.min_heap = []
    
    def addNum(self, num: int) -> None:
        if not self.max_heap or -self.max_heap[0] > num:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)

        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        elif len(self.max_heap) < len(self.min_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
    
    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        return -self.max_heap[0]


class SlidingWindowMedian480:
    def medianSlidingWindow(self, nums: list[int], k: int) -> list[float]:
        """
        Finds the median of each sliding window of size k in the given list of numbers.

        Args:
            nums (list[int]): The list of integers.
            k (int): The size of the sliding window.

        Returns:
            list[float]: A list containing the medians of each sliding window.

        TC: O(n log k), where n is the length of nums and k is the window size.
        SC: O(k), for storing the current window elements.
        """
        def rebalance_heap():
            if len(max_heap) > len(min_heap) +1:
                heapq.heappush(min_heap, -heapq.heappop(max_heap))
            elif len(max_heap) < len(min_heap):
                heapq.heappush(max_heap, -heapq.heappop(min_heap))
        
        def remove_old_entry(heap, target):
            index = heap.index(target)
            heap[index] = heap[-1]
            del heap[-1]
            heapq.heapify(heap)
        
        max_heap = []
        min_heap = []
        result = [0.0 for x in range(len(nums) - k + 1)]
        
        for i in range(len(nums)):
            if not max_heap or -max_heap[0] >= nums[i]:
                heapq.heappush(max_heap, -nums[i])
            else:
                heapq.heappush(min_heap, nums[i])
            
            rebalance_heap()

            current_index = i - k + 1

            if current_index >= 0:
                if len(max_heap) == len(min_heap):
                    result[current_index] = (max_heap[0] + min_heap[0]) / 2
                else:
                    result[current_index] = -max_heap[0]
                    
                remove_target = nums[current_index]

                if remove_target <= -max_heap[0]:
                    remove_old_entry(max_heap, -remove_target)
                else:
                    remove_old_entry(min_heap, remove_target)
                
                rebalance_heap()

        return result