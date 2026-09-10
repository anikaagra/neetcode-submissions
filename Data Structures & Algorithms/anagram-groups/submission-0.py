class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_to_og = {}
        res = []

        for s in strs:
            word = "".join(sorted(s))
            if word not in sorted_to_og:
                sorted_to_og[word] = [s]
            else:
                sorted_to_og[word].append(s)

        for word in sorted_to_og:
            res.append(sorted_to_og[word])

        return res