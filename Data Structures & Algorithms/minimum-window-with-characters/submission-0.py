class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        need = defaultdict(int)
        for char in t:
            need[char] += 1
        needed_chars = len(need)

        have = defaultdict(int)
        have_chars = 0
        
        best, best_len = [-1, -1], float("inf")
        l = 0

        for r in range(len(s)):
            c = s[r]
            have[c] += 1

            if c in need and need[c] == have[c]:
                have_chars += 1
        
            while have_chars == needed_chars:
                if (r - l + 1) < best_len:
                    best = [l, r]
                    best_len = r - l + 1
                have[s[l]] -= 1
                if s[l] in need and need[s[l]] > have[s[l]]:
                    have_chars -= 1
                l += 1
        
        l, r = best
        return s[l:r + 1] if best_len != float("inf") else ""