from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_chars = defaultdict(int)

        for letter in s:
            s_chars[letter] += 1
        
        for letter in t:
            if s_chars[letter] == 0:
                return False
            s_chars[letter] -= 1

        return True
