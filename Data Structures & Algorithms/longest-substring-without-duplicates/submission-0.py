class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        max_substring_len = 0

        for i in range(n - 2):
            curr_set = set()
            curr_set.add(s[i])
            last_i = i + 1

            while last_i < n and s[last_i] not in curr_set:
                curr_set.add(s[last_i])
                last_i += 1
            max_substring_len = max(max_substring_len, last_i - i)

        return max_substring_len