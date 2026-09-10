class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(node):
            nonlocal ans

            if not node:
                return 0, 0

            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)

            total = left_sum + right_sum + node.val
            count = left_count + right_count + 1

            if total // count == node.val:
                ans += 1

            return total, count

        dfs(root)
        return ans