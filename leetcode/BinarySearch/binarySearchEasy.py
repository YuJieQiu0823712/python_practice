class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class EasySolution:
    def closestBinarySearchTreeValue270(self, root: TreeNode, target: float) -> int:
        """
        Finds the value in a Binary Search Tree that is closest to the target.

        Args:
            root (TreeNode): The root of the binary search tree.
            target (float): The target value to find the closest match for.

        Returns:
            int: The value in the BST that is closest to the target.
        
        TC: O(n)
        SC: O(n) 
        """
        res = root.val
        while root:
            if abs(target - root.val) < abs(target - res):
                res = root.val
            if root.val < target:
                root = root.right
            else:
                root = root.left
        return res


    def isBadVersion(self, version: int) -> bool:
        """
        Mock API to be overwritten in tests.
        """
        raise NotImplementedError("This method should be mocked in tests.")
        
    def firstBadVersion278(self, n: int) -> int:
        """
        Finds the first bad version in a sequence of versions.

        Args:
            n (int): The total number of versions.

        Returns:
            int: The first bad version.
        
        Note:
            This function assumes that the API isBadVersion(version) is available.
        
        TC: O(log n)
        SC: O(1)
        """
        low = 1
        high = n
        while low <= high:
            mid = (high - low) // 2 + low # prevent integer overflow
            if self.isBadVersion(mid):
                high = mid - 1
            else:
                low = mid + 1
        return low

    
    def intersectionOfTwoArrays349(self, nums1: list[int], nums2: list[int]) -> list[int]:
        """
        Finds the intersection of two arrays.

        Args:
            nums1 (list[int]): The first array.
            nums2 (list[int]): The second array.

        Returns:
            list[int]: A list containing the intersection of the two arrays.
        
        TC: O(n log n)
        SC: O(n)
        """

        nums1.sort()
        nums2.sort()
        res = []
        for num in nums1:
            low = 0
            hight = len(nums2) - 1

            while low <= high:
                mid = (high - low) // 2 + low

                if num == nums[mid] and num not in res:
                    res.append(num)
                elif nums2[mid] > num:
                    high = mid - 1
                else:
                    low = mid + 1
        return res



    
