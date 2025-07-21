import heapq
import collections


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




class MediumSolution:
    def kthLargestElementInAnArray215(self, nums: list[int], k: int) -> int:
        """
        Finds the kth largest element in an unsorted array.

        Args:
            nums (list[int]): The unsorted array.
            k (int): The kth position to find.

        Returns:
            int: The kth largest element.
        
        TC: O(n log k), where n is the number of elements in nums.
        SC: O(k), due to the min-heap storing up to k elements.
        """
        min_heap = []
        for num in nums:
            if len(min_heap) < k:
                heapq.heappush(min_heap, num) 
                # Default heap in Python is a min-heap, so the smallest element is always at heap[0].
            else:
                heapq.heappushpop(min_heap, num)
        return min_heap[0]

    
    def taskScheduler621(self, tasks: list[str], n: int) -> int:
        """
        Calculates the least number of intervals needed to finish all tasks with cooldown.

        Each same task must be executed at least `n` intervals apart. The CPU can remain idle
        if there are no eligible tasks to run during an interval.

        Args:
            tasks (list[str]): A list of tasks represented by capital letters.
            n (int): The non-negative cooling interval between same tasks.

        Returns:
            int: The minimum number of intervals required to finish all tasks.

        TC: O(n log k), where n is the number of tasks and k is the number of unique tasks.
        SC: O(k), where k is the number of unique tasks.   
        """
    
        tasks_count = collections.Counter(tasks).values()
        max_heap = []
        count = 0

        for value in tasks_count:
            heapq.heappush(max_heap, -value)  # Use negative values for max-heap behavior
        
        while max_heap:
            remain_tasks = []

            for _ in range(n+1):
                count += 1
                
                if max_heap:
                    curr_tasks_value = -heapq.heappop(max_heap)
                    # Pop the largest task count (most frequent task)
                    if curr_tasks_value - 1 > 0:
                        remain_tasks.append(curr_tasks_value - 1)
                if not max_heap and not remain_tasks:
                    return count
            
            for task in remain_tasks:
                heapq.heappush(max_heap, -task)

    
        


