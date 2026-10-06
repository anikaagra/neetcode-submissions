from collections import defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        n = len(wordList)
        m = len(wordList[0])

        adj_list = defaultdict(list)
        sets = [defaultdict(list) for i in range(m)]

        for char in range(m):
            for word in wordList:
                sub = word[:char] + "." + word[char+1:]
                for w in sets[char][sub]:
                    adj_list[w].append(word)
                    adj_list[word].append(w)
                sets[char][sub].append(word)

        q = deque()
        visited = set()

        for char in range(m):
            sub = beginWord[:char] + "." + beginWord[char+1:]
            if sub in sets[char]:
                for w in sets[char][sub]:
                    q.append((w, 2))
        
        while q:
            curr_word, dist = q.popleft()
            if curr_word == endWord:
                return dist
            visited.add(curr_word)
            for w in adj_list[curr_word]:
                if w not in visited:
                    q.append((w, dist + 1))
        return 0        
        