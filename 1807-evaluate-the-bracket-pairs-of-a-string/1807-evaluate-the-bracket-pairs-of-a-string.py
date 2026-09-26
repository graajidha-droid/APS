class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        d = {key: value for key, value in knowledge}

        i = 0
        ans = []

        while i < len(s):
            if s[i] == '(':
                j = s.find(')', i + 1)
                key = s[i + 1:j]

                ans.append(d.get(key, '?'))
                i = j
            else:
                ans.append(s[i])

            i += 1

        return ''.join(ans)