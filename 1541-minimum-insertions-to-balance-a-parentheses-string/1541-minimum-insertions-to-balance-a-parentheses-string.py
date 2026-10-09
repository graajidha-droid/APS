class Solution:
    def minInsertions(self, s: str) -> int:
        insertions = 0
        open_needed = 0  # Tracks unmatched '('
        i = 0
        n = len(s)
        
        while i < n:
            if s[i] == '(':
                open_needed += 1
                i += 1
            else:  # s[i] == ')'
                # Check if there is a consecutive second ')'
                if i + 1 < n and s[i + 1] == ')':
                    i += 2  # Consumed "))"
                else:
                    insertions += 1  # Insert a missing ')' to form "))"
                    i += 1  # Consumed single ')' + inserted ')'
                
                # Pair the "))" with an opening '('
                if open_needed > 0:
                    open_needed -= 1
                else:
                    insertions += 1  # Insert a missing '(' before "))"
        
        # Each remaining unmatched '(' needs two ')'
        insertions += open_needed * 2
        
        return insertions