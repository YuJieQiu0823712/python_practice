class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class MediumSolution:    
    def pathSum113(self, root: TreeNode, targetSum: int) -> list[list[int]]:
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