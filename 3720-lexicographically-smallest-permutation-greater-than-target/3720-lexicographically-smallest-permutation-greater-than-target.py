class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        count = [0] * 26

        for ch in s:
            count[ord(ch) - ord('a')] += 1

        ans = []

        for i in range(len(target)):
            x = ord(target[i]) - ord('a')

            if count[x] > 0:
                ans.append(target[i])
                count[x] -= 1
            else:
                break
        else:
            i = len(target)

        while i >= 0:
            if i < len(target):
                start = ord(target[i]) - ord('a') + 1

                for j in range(start, 26):
                    if count[j] > 0:
                        result = ans + [chr(j + ord('a'))]
                        count[j] -= 1

                        for k in range(26):
                            result.extend([chr(k + ord('a'))] * count[k])

                        return "".join(result)

            if not ans:
                break

            ch = ans.pop()
            count[ord(ch) - ord('a')] += 1
            i -= 1

        return ""