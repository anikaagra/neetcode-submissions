class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = {}
        l = 0
        out = 0

        for r, c in enumerate(s):
            if c in visited:
                l = max(l, visited[c] + 1)
            visited[c] = r
            out = max(out, r - l + 1)

        return out 