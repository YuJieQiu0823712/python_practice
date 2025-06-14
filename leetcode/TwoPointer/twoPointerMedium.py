class MediumSolution:
    def twoSumIIInputArrayIsSorted167(self, numbers:list[int], target: int) -> list[int]:
        """
        Finds two numbers in a sorted array that add up to a specific target.

        Given a 1-indexed array of integers `numbers` that is already sorted in
        non-decreasing order, returns the indices of the two numbers such that 
        they add up to the target.

        Assumes exactly one solution exists, and the same element cannot be used twice.

        Args:
            numbers (List[int]): A list of integers sorted in ascending order.
            target (int): The target sum to find.

        Returns:
            List[int]: A list containing the 1-based indices of the two numbers 
                       that add up to the target. Returns [-1, -1] if no such pair exists.
        """
        point_a = 0
        point_b = len(numbers) - 1

        while point_a < point_b:
            curr_num = numbers[point_a] + numbers[point_b]
            
            if curr_num == target:
                return [point_a +1, point_b + 1]
            if curr_num < target:
                point_a += 1
            else:
                point_b -= 1
        return [-1, -1]