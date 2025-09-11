class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class MediumSolution:    
    def pathSumII113(self, root: TreeNode, targetSum: int) -> list[list[int]]:
        """
        TC: O(n^2)
        SC: O(n)
        """
        def find_path(curr_node, target_sum, curr_path, all_paths):
            if not curr_node:
                return

            curr_path.append(curr_node.val)

            # Base case
            if not curr_node.left and not curr_node.right and curr_node.val == target_sum:
                all_paths.append(list(curr_path))
                # for item in curr_path:
                #   temp = []
                #   temp.append(item)
                #   all_paths.append(temp)
            else:
                target_sum -= curr_node.val
                find_path(curr_node.left, target_sum, curr_path, all_paths)
                find_path(curr_node.right, target_sum , curr_path, all_paths)

            # Backtrack
            curr_path.pop()
        all_paths = []
        find_path(root, targetSum, [], all_paths)
        return all_paths
    
    def pathSumIII437(self, root: TreeNode, targetSum: int) -> int:
        """
        TC: O(n^2)
        SC: O(n)
        """
        def find_path(curr_node, target_sum, curr_path):
            if not curr_node:
                return 0

            curr_path.append(curr_node.val)
            path_count = 0
            path_sum = 0

            for i in range(len(curr_path)-1, -1, -1):
                path_sum += curr_path[i]
                if path_sum == target_sum:
                    path_count += 1

            path_count += find_path(curr_node.left, target_sum, curr_path)
            path_count += find_path(curr_node.right, target_sum, curr_path)

            curr_path.pop()
            return path_count

        return find_path(root, targetSum, [])