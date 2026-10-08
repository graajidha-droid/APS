class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        # Step 1: Calculate minimum removals needed
        left_rem = 0
        right_rem = 0
        
        for char in s:
            if char == '(':
                left_rem += 1
            elif char == ')':
                if left_rem > 0:
                    left_rem -= 1
                else:
                    right_rem += 1

        res = []

        # Step 2: DFS to generate valid expressions
        def backtrack(index, left_count, right_count, left_rem, right_rem, path):
            if index == len(s):
                if left_rem == 0 and right_rem == 0:
                    res.append("".join(path))
                return

            char = s[index]

            # Pruning: skip unnecessary branching
            if (char == '(' and left_rem < 0) or (char == ')' and right_rem < 0):
                return

            # Option 1: Skip current parenthesis (if removals are available)
            if char == '(' and left_rem > 0:
                # Skip duplicate consecutive '('
                if index == 0 or s[index - 1] != '(' or path and path[-1] == '(':
                    backtrack(index + 1, left_count, right_count, left_rem - 1, right_rem, path)
            
            elif char == ')' and right_rem > 0:
                # Skip duplicate consecutive ')'
                if index == 0 or s[index - 1] != ')' or path and path[-1] == ')':
                    backtrack(index + 1, left_count, right_count, left_rem, right_rem - 1, path)

            # Option 2: Keep current character
            path.append(char)
            if char not in '()':
                backtrack(index + 1, left_count, right_count, left_rem, right_rem, path)
            elif char == '(':
                backtrack(index + 1, left_count + 1, right_count, left_rem, right_rem, path)
            elif char == ')' and left_count > right_count:
                backtrack(index + 1, left_count, right_count + 1, left_rem, right_rem, path)
            path.pop()

        # Alternative cleaner backtracking implementation
        def dfs(idx, l_rem, r_rem, open_cnt, expr):
            if idx == len(s):
                if l_rem == 0 and r_rem == 0 and open_cnt == 0:
                    res.append(expr)
                return

            c = s[idx]

            # Option to discard current character
            if (c == '(' and l_rem > 0) or (c == ')' and r_rem > 0):
                dfs(
                    idx + 1,
                    l_rem - (1 if c == '(' else 0),
                    r_rem - (1 if c == ')' else 0),
                    open_cnt,
                    expr
                )

            # Option to keep current character
            if c not in '()':
                dfs(idx + 1, l_rem, r_rem, open_cnt, expr + c)
            elif c == '(':
                dfs(idx + 1, l_rem, r_rem, open_cnt + 1, expr + c)
            elif c == ')' and open_cnt > 0:
                dfs(idx + 1, l_rem, r_rem, open_cnt - 1, expr + c)

        ans = set()
        
        def backtrack_simple(idx, l_rem, r_rem, open_cnt, path):
            if idx == len(s):
                if l_rem == 0 and r_rem == 0 and open_cnt == 0:
                    ans.add("".join(path))
                return

            c = s[idx]

            # Delete '(' or ')'
            if c == '(' and l_rem > 0:
                backtrack_simple(idx + 1, l_rem - 1, r_rem, open_cnt, path)
            if c == ')' and r_rem > 0:
                backtrack_simple(idx + 1, l_rem, r_rem - 1, open_cnt, path)

            # Keep character
            path.append(c)
            if c not in '()':
                backtrack_simple(idx + 1, l_rem, r_rem, open_cnt, path)
            elif c == '(':
                backtrack_simple(idx + 1, l_rem, r_rem, open_cnt + 1, path)
            elif c == ')' and open_cnt > 0:
                backtrack_simple(idx + 1, l_rem, r_rem, open_cnt - 1, path)
            path.pop()

        backtrack_simple(0, left_rem, right_rem, 0, [])
        return list(ans)