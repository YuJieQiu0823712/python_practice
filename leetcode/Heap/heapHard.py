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

    
class HardSolution:
    def minPushBox1263(self, grid: list[list[str]]) -> int:
        """
        Finds the minimum pushes required to move the box to the target.

        The grid consists of walls (`#`), empty spaces (`.`), the player (`S`), 
        the box (`B`), and the target (`T`). The player can move freely in empty 
        spaces and can push the box if standing next to it. The goal is to 
        determine the minimum number of pushes needed to move the box to the target.

        This implementation uses BFS + Dijkstra (priority queue). States are 
        represented as a tuple: (push_count, player_row, player_col, box_row, box_col).

        Args:
            grid (list[list[str]]): 2D grid containing the map of the problem.
                - "#" = wall
                - "." = empty cell
                - "S" = player
                - "B" = box
                - "T" = target

        Returns:
            int: Minimum number of pushes required to move the box to the target.
            Returns -1 if it is impossible.

        TC:
            O(M^2 * N^2 * log(MN)), where M = number of rows and N = number of columns.
            - Each state is defined by (player, box), so total states = O(M^2 * N^2).
            - For each state, we expand 4 possible moves.
            - Heap operations take O(log(MN)).

        SC:
            O(M^2 * N^2).
            - Graph storage: O(MN).
            - Visited states: O(M^2 * N^2).
            - Heap may also store up to O(M^2 * N^2) states.
        """
        
        player = None
        box = None
        target = None
        graph = set()
        visited = set()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "#":
                    continue
                if grid[r][c] == "S":
                    player = (r, c)
                if grid[r][c] == "B":
                    box = (r, c)
                if grid[r][c] == "T":
                    target = (r, c)
                graph.add((r, c))
        
        min_heap = [(0, *player, *box)] # * pass tuple elements as separate arguments

        while min_heap:
            pushes, curr_player_row, curr_player_col, curr_box_row, curr_box_col = heapq.heappop(min_heap)
            if (curr_box_row, curr_box_col) == target:
                return pushes
            if (curr_player_row, curr_player_col, curr_box_row, curr_box_col) in visited:
                continue
            visited.add((curr_player_row, curr_player_col, curr_box_row, curr_box_col))
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for row, col in directions:
                next_player_pos = (curr_player_row + row, curr_player_col + col)
                next_box_pos = (curr_box_row + row, curr_box_col + col)
                if next_player_pos == (curr_box_row, curr_box_col) and next_box_pos in graph:
                   heapq.heappush(min_heap, (pushes + 1, *next_player_pos, *next_box_pos))
                elif next_player_pos != (curr_box_row, curr_box_col) and next_player_pos in graph:
                    heapq.heappush(min_heap, (pushes, *next_player_pos, curr_box_row, curr_box_col)) 
        return -1
            