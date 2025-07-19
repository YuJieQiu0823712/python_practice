import heapq

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
            else:
                heapq.heappushpop(min_heap, num)
        return min_heap[0]
