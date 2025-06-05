class MediumSolution:
    def basic1(self, k: int, arr: list[int]) -> list[int]:
        """
        Return the average of every contiguous subarray of size k in the given array.
        Args:
            k (int): Size of the subarray.
            arr (list[int]): Input array.
        
        Returns:
            list[int]: List of averages of each contiguous subarray of size k.

        TC: O(n)
        SC: O(n)
        """
        result = []
        start = 0
        sum = 0
        for end in range(len(arr)):
            sum += arr[end]
            if end >= k-1:
                result.append(sum/k)
                sum -= arr[start]
                start += 1
        return result

    def basic2(self, k: int, arr: list[int]) -> int:
        """
        Return the maximum sum of any contiguous subarray of size k in the given array.
        Args:
            k (int): Size of the subarray.
            arr (list[int]): Input array.
        
        Returns:
            int: Maximum sum of any contiguous subarray of size k.

        TC: O(n)
        SC: O(1)
        """
        max_sum = 0
        curr_sum = 0
        start = 0
        
        for end in range(len(arr)):
            curr_sum += arr[end]
            if end >= k-1:
                max_sum = max(max_sum, curr_sum)
                curr_sum -= arr[start]
                start += 1
        return max_sum
   


    def fruitIntoBaskets904(self, tree: list[int]) -> int:
        """
        Given a list of integers representing types of fruits on trees arranged in a row,
        this function returns the length of the longest subarray with at most two distinct
        types of fruits. This simulates the process of collecting fruits using two baskets,
        where each basket can hold only one type of fruit.

        Parameters:
        -----------
        tree : list[int]
            A list of integers where each integer represents a type of fruit.

        Returns:
        --------
        int
            The maximum number of fruits that can be collected in two baskets from a
            contiguous section of the tree row.
        TC: O(n)
        SC: O(1)
        """
        start = 0
        curr_fruits = 0
        max_fruits = 0
        basket = {}

        for end in range(len(tree)):
            curr_fruits += 1
            basket[tree[end]] = basket.get(tree[end], 0) + 1

            while len(basket) > 2:
                curr_fruits -= 1
                basket[tree[start]] -= 1
                if basket[tree[start]] == 0:
                    del basket[tree[start]]
                start += 1
            max_fruits = max(max_fruits, curr_fruits)
        return max_fruits
