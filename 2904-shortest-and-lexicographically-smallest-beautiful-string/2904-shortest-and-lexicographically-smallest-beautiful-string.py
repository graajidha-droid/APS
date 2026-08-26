class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        left = 0
        count = 0
        ans = ""

        for right in range(len(s)):
            if s[right] == "1":
                count += 1

            while count > k:
                if s[left] == "1":
                    count -= 1
                left += 1

            while count == k and s[left] == "0":
                left += 1

            if count == k:
                current = s[left:right + 1]

                if ans == "" or len(current) < len(ans):
                    ans = current
                elif len(current) == len(ans) and current < ans:
                    ans = current

        return ans