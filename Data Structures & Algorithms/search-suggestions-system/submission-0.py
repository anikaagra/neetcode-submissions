class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        out = []
        prefix = []
        start = 0

        def binary_search(target, start):
            l, r = start, len(products)
            while l < r:
                m = (l + r - 1)//2
                if products[m] >= target:
                    r = m
                else:
                    l = m + 1
            return l

        for i in range(len(searchWord)):
            prefix.append(searchWord[i])
            start = binary_search("".join(prefix), start)

            cur = []
            for j in range(start, min(start + 3, len(products))):
                if products[j].startswith("".join(prefix)):
                    cur.append(products[j])
                else:
                    break
            
            out.append(cur)

        return out