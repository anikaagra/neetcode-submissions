class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        i = 0
        max_substring_len = 0
        mp = {}

        for j in range(n):
            if s[j] in mp:
                i = max(i, mp[s[j]] + 1)
            mp[s[j]] = j
            max_substring_len = max(max_substring_len, j - i + 1)

        return max_substring_len