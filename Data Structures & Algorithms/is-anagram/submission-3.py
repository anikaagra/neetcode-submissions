from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # create hashmap of s chars to # 
        # compare and subtract by one for t chars --> if # is 0 or not in map --> false
        # O(max(len(s), len(t))) --> O(n)

        s_chars = defaultdict(int)

        for letter in s:
            s_chars[letter] += 1
        
        print(s_chars)
        
        for letter in t:
            if s_chars[letter] == 0:
                return False
            s_chars[letter] -= 1
        return True
