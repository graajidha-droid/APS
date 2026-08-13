class Solution:
    def longestRepeating(self, s: str, queryCharacters: str,
                         queryIndices: List[int]) -> List[int]:

        n = len(s)
        s = list(s)

        left = [0] * (4 * n)
        right = [0] * (4 * n)
        best = [0] * (4 * n)
        size = [0] * (4 * n)

        def pull(node, l, r):
            mid = (l + r) // 2
            a = node * 2
            b = node * 2 + 1

            size[node] = size[a] + size[b]
            left[node] = left[a]
            right[node] = right[b]
            best[node] = max(best[a], best[b])

            if s[mid] == s[mid + 1]:
                best[node] = max(best[node], right[a] + left[b])

                if left[a] == size[a]:
                    left[node] += left[b]

                if right[b] == size[b]:
                    right[node] += right[a]

        def build(node, l, r):
            if l == r:
                left[node] = right[node] = best[node] = size[node] = 1
                return

            mid = (l + r) // 2

            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)

            pull(node, l, r)

        def update(node, l, r, index):
            if l == r:
                return

            mid = (l + r) // 2

            if index <= mid:
                update(node * 2, l, mid, index)
            else:
                update(node * 2 + 1, mid + 1, r, index)

            pull(node, l, r)

        build(1, 0, n - 1)

        answer = []

        for index, ch in zip(queryIndices, queryCharacters):
            s[index] = ch
            update(1, 0, n - 1, index)
            answer.append(best[1])

        return answer