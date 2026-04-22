class Solution(object):
    def pathSum(self, root, targetSum):
        result = []

        def dfs(node, remaining_sum, path):
            if not node:
                return

            # Add current node
            path.append(node.val)

            # Check if it's a leaf and sum is matched
            if not node.left and not node.right and remaining_sum == node.val:
                result.append(list(path))  # copy path

            else:
                dfs(node.left, remaining_sum - node.val, path)
                dfs(node.right, remaining_sum - node.val, path)

            # Backtrack
            path.pop()

        dfs(root, targetSum, [])
        return result