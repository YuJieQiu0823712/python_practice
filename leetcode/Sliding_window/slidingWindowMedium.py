import math

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
   
    def minSubArrayLen209(self, target: int, nums: list[int]) -> int:
        """
        Finds the minimal length of a contiguous subarray of which the sum is 
        greater than or equal to the given target value.

        This implementation uses the sliding window technique for optimal performance.

        Args:
            target (int): The target sum that the subarray needs to reach or exceed.
            nums (list[int]): A list of positive integers.

        Returns:
            int: The length of the smallest contiguous subarray with a sum >= target.
                Returns 0 if no such subarray exists.
                
        TC: O(n)
        SC: O(1)
        """
        curr_sum = 0
        start = 0
        curr_length = 0
        output = math.inf

        for end in range(len(nums)):
            curr_sum += nums[end]
            curr_length += 1
            while curr_sum >= target:
                output = min(output, curr_length)
                curr_sum -= nums[start]
                curr_length -= 1
                start += 1   
        if output == math.inf:
            return 0
        return output       

    def longestSubstringWithAtMostKDistinctCharacters340(self, string: str, k: int) -> int: 
        """
        Given a string, find the longest substring with no more than k distinct characters.

        args:
            string (str): The input string.
            k (int): The maximum number of distinct characters allowed in the substring.

        Returns:
            int: The length of the longest substring with at most k distinct characters.
        
        TC: O(n)
        SC: O(k)
        """
        start = 0
        length = 0
        max_length = 0
        lookup = {}
        for end in range(len(string)):
            right_char = string[end]
            lookup[right_char] = lookup.get(right_char, 0) + 1
            # 0 if the key wasn't there
            length += 1
            while len(lookup) > k:
                left_char = string[start]
                lookup[left_char] -= 1
                if lookup[left_char] == 0:
                    del lookup[left_char]
                start += 1
                length -= 1
            max_length = max(max_length, length)
        return max_length     


    def fruitIntoBaskets904(self, fruits: list[int]) -> int:
        """
        Given a list of integers representing types of fruits arranged in a row,
        this function returns the length of the longest subarray with at most two distinct
        types of fruits. This simulates the process of collecting fruits using two baskets,
        where each basket can hold only one type of fruit.

        Args:
            fruits (list[int]): A list of integers where each integer represents a type of fruit.

        Returns:
            int: The maximum number of fruits that can be collected in two baskets from a
                contiguous section of the fruits row.

        TC: O(n)
        SC: O(1)
        """
        start = 0
        curr_fruits = 0
        max_fruits = 0
        basket = {}

        for end in range(len(fruits)):
            curr_fruits += 1
            basket[fruits[end]] = basket.get(fruits[end], 0) + 1

            while len(basket) > 2:
                curr_fruits -= 1
                basket[fruits[start]] -= 1
                if basket[fruits[start]] == 0:
                    del basket[fruits[start]]
                start += 1
            max_fruits = max(max_fruits, curr_fruits)
        return max_fruits

    def longestSubstringWithoutRepeatingCharacters3(self, s: str) -> int:
        """
        Given a string, find the length of the longest substring without repeating characters.

        Args:
            s (str): The input string.

        Returns:
            int: The length of the longest substring without repeating characters.
        
        TC: O(n)
        SC: O(min(n, m)) where m is the size of the character set
        """
        left = 0
        max_length = 0
        index_lookup = {}
        for right in range(len(s)):
            if s[right] in index_lookup:
                left = max(left, index_lookup[s[right]] + 1)
                # index_lookup[s[right]] is the index of the previous occurrence of the character.
                # Must move one character past it, hence the +1.
            index_lookup[s[right]] = right
            max_length = max(max_length, right - left + 1)
        return max_length

    def longestRepeatingCharacterReplacement424(self, s: str, k: int) -> int:
        """
        Given a string s and an integer k, find the length of the longest substring that can be obtained
        by replacing at most k characters in the string with any character.

        Args:
            s (str): The input string.
            k (int): The maximum number of characters that can be replaced.

        Returns:
            int: The length of the longest substring after replacements.
        
        TC: O(n)
        SC: O(1)
        """
        max_length = 0
        max_repeat = 0
        start = 0
        lookup = {}

        for end in range(len(s)):
            lookup[s[end]] = lookup.get(s[end], 0) + 1
            max_repeat = max(max_repeat, lookup[s[end]])
            if (end - start + 1 - max_repeat) > k: #
                lookup[s[start]] -= 1
                start += 1
            max_length = max(max_length, end - start + 1)
        return max_length

    
    def maxConsecutiveOnesIII1004(self, nums: list[int], k: int) -> int:
        """
        Returns the length of the longest subarray containing only 1s after flipping at most `k` 0s to 1s.

        This function uses the sliding window technique to find the maximum number of consecutive 1s
        in the binary array `nums`, allowing up to `k` zeros to be flipped to 1s.

        Args:
            nums (list[int]): A list of integers consisting only of 0s and 1s.
            k (int): The maximum number of 0s allowed to be flipped.

        Returns:
            int: The maximum length of a subarray with only 1s after flipping at most `k` zeros.

        TC: O(n)
        SC: O(1)
        """
        start = 0
        max_length = 0
        zero = 0
        for end in range(len(nums)):
            if nums[end] == 0:
                zero += 1
            while zero > k:
                if nums[start] == 0:
                    zero -= 1
                start += 1
                max_length = max(max_length, end - start + 1)
        return max_length

    def permutationInString567(self, str: str, pattern: str) -> bool:
        """
        Check if one string is a permutation of another string.

        Args:
            s1 (str): The first string.
            s2 (str): The second string.

        Returns:
            bool: True if s2 contains a permutation of s1, False otherwise.
        
        TC: O(n)
        SC: O(n)
        """
        start = 0
        lookup = {}
        matched = 0
        for item in pattern:
            lookup[item] = lookup.get(item, 0) + 1
        for end in range(len(str)):
            if str[end] in lookup:
                lookup[str[end]] -= 1
                if lookup[str[end]] == 0:
                    matched += 1
                if matched == len(lookup):
                    return True
                if end >= len(pattern)-1:
                    if str[start] in lookup:
                        if lookup[str[start]] == 0:
                            matched -= 1
                        lookup[str[start]] += 1
                    start += 1    
        return False
    
        

