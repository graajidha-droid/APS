class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        count = [0] * 26

        for ch in s:
            count[ord(ch) - ord('a')] += 1

        # A palindrome can have at most one odd frequency
        if sum(x % 2 for x in count) > 1:
            return ""

        middle = ""

        for i in range(26):
            if count[i] % 2:
                middle = chr(ord('a') + i)

        half = [x // 2 for x in count]
        length = len(s) // 2
        prefix = []

        def possible():
            left = "".join(prefix)

            # Make the largest possible remaining left half
            for i in range(25, -1, -1):
                left += chr(ord('a') + i) * half[i]

            palindrome = left + middle + left[::-1]

            return palindrome > target

        for _ in range(length):
            found = False

            for i in range(26):
                if half[i] == 0:
                    continue

                half[i] -= 1
                prefix.append(chr(ord('a') + i))

                if possible():
                    found = True
                    break

                prefix.pop()
                half[i] += 1

            if not found:
                return ""

        left = "".join(prefix)
        answer = left + middle + left[::-1]

        return answer if answer > target else ""