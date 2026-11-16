from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        out = []

        for s in strs:
            key = ''.join(sorted(s))
            anagrams[key].append(s)
        
        for key in anagrams.keys():
            out.append(anagrams[key])
        
        return out