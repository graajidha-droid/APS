class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        def dfs(exp):
            j = exp.find('}')

            if j == -1:
                result.add(exp)
                return

            i = exp.rfind('{', 0, j)

            left = exp[:i]
            middle = exp[i + 1:j]
            right = exp[j + 1:]

            for part in middle.split(','):
                dfs(left + part + right)

        result = set()
        dfs(expression)

        return sorted(result)