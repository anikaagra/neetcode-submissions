class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        reverse_s = s[::-1]
        return self.longestCommonSubsequence(s, reverse_s)
    
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # space optimized dp where n is the longer text and m is shorter
        # prev[j] represents the lcs for text1[i+1:] compared to all text2[j:]
        # curr[j] represents the lcs for text1[i:] compared to all text2[j:]

        if len(text1) < len(text2):
            text1, text2 = text2, text1

        n = len(text1)
        m = len(text2)

        prev = [0] * (m + 1)
        curr = [0] * (m + 1)
        
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if text1[i] == text2[j]:
                    curr[j] = prev[j+1] + 1
                else:
                    curr[j] = max(curr[j + 1], prev[j])
            prev, curr = curr, prev
        
        return prev[0]