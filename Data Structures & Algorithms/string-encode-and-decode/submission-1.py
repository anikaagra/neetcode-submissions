class Solution:

    def encode(self, strs: List[str]) -> str:
        return " ".join(f"{str(len(s))},{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []

        while i < len(s):
            j = s.find(",", i)
            l = int(s[i:j])
            res.append(s[j+1:j+l+1])
            i = j + l + 1
        return res
