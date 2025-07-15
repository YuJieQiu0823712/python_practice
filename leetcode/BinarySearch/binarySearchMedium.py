class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class MediumSolution:
   
    def findFirstAndLastPositionOfElementInSortedArray34(self, nums: list[int], target: int) -> list[int]:
        """
        Finds the first and last position of a target value in a sorted array.

        Args:
            nums (list[int]): The sorted array.
            target (int): The target value to find.

        Returns:
            list[int]: A list containing the first and last positions of the target.
        
        TC: O(log n)
        SC: O(1)
        """
        def binary_search(nums, target, look_for_right_most):
            low = 0
            high = len(nums) - 1
            target_idx = -1
            while low <= high:
                mid = (high - low) // 2 + low
                if nums[mid] < target:
                    low = mid +1
                elif nums[mid] > target:
                    high = mid - 1
                else:
                    target_idx = mid
                    if look_for_right_most:
                        low = mid + 1
                    else:
                        high = mid - 1
            return target_idx
        
        left = binary_search(nums, target, False)
        right = binary_search(nums, target, True)
        return [left, right]

    
    def searchInRotatedSortedArray33(self, nums: list[int], target: int) -> int:
        """
        Searches for a target value in a rotated sorted array.

        Args:
            nums (list[int]): The rotated sorted array.
            target (int): The target value to search for.

        Returns:
            int: The index of the target value if found, otherwise -1.
        
        TC: O(log n)
        SC: O(1)
        """
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (high - low) // 2 + low

            if nums[mid] == target:
                return mid
                
            elif nums[low] < nums[mid]:
                if nums[low] == target:
                    return low
                elif nums[low] < target and target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[high] == target:
                    return high
                elif nums[mid] < target and target < nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1 
           

    def balanceABinarySearchTree1382(self, root: TreeNode) -> TreeNode:
        """
        Rebuild an arbitrary Binary Search Tree into a height-balanced BST
        (i.e. the depths of the two child sub-trees of every node never differ by more than 1).
        
        Strategy:        
            1. **In-order traversal** collects the tree’s nodes into a sorted list.
            2. **Divide-and-conquer** recursively picks the middle element as root
            to build a perfectly balanced tree (the classic “sorted-array-to-BST” trick).

        Args:
            root (TreeNode): The root of the BST.

        Returns:
            TreeNode: The root of the balanced BST.
        
        TC: O(n) every node is visited a constant number of times.
        SC: O(n) the auxiliary list of nodes.
        """
        def dfs_inorder(node):
            if not node:
                return
            dfs_inorder(node.left)
            nodes.append(node)
            dfs_inorder(node.right)
        def _balance_bs_tree(left, right):
            if left > right:
                return
            mid = (left + right) // 2
            root = nodes[mid]
            root.left = _balance_bs_tree(left, mid - 1)
            root.right = _balance_bs_tree(mid + 1, right)
            return root
        nodes = []
        dfs_inorder(root)
        return _balance_bs_tree(0, len(nodes) - 1)
            

    def missingElementInSortedArray1060(self, nums: list[int], k: int) -> int:
        """
        Finds the kth missing element in a sorted array.

        Strategy:
            This solution uses **binary search** to find the smallest index `left`
            such that the number of missing integers up to `nums[left]` is
            greater than or equal to `k`.

            The number of missing elements before index `i` is calculated as:
                missing_count(i) = nums[i] - nums[0] - i

            This formula works because in a perfect sequence starting from `nums[0]`,
            the value at index `i` should be `nums[0] + i`. The difference between
            this expected value and the actual value `nums[i]` reveals how many
            values are missing up to that point.

            After binary search:
            - `left` is the index where the k-th missing number would be inserted.
            - The final result is computed using:
                nums[0] + k + left - 1

            This formula adds the total number of missing elements to the starting
            value, adjusted by the number of known values scanned (`left`), and
            corrected for zero-based indexing.
            
        Args:
            nums (list[int]): The sorted array.
            k (int): The kth missing element to find.

        Returns:
            int: The kth missing element.
        
        TC: O(log n)
        SC: O(1)
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (right + left) // 2
            missing_count= nums[mid] - nums[0] - mid
            if missing_count < k:
                left = mid + 1
            else:
                right = mid - 1
        return nums[0] + k + left -1 
        # index start from 0, so we need to adjust the index by subtracting 1
    



    
