class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # bfs
        if "0000" in deadends:
            return -1
            
        q = deque([("0000", 0)])
        res = 0
        visited = set()

        for deadend in deadends:
            visited.add(deadend)

        def children(lock):
            out = []
            for i in range(4):
                dig = str((int(lock[i]) + 1) % 10)
                out.append(lock[:i] + dig + lock[i+1:])
                dig = str((int(lock[i]) - 1 + 10) % 10)
                out.append(lock[:i] + dig + lock[i+1:])
            return out

        while q:
            comb, turns = q.popleft()
            if comb == target:
                return turns
            for child in children(comb):
                if child not in visited:
                    visited.add(child)
                    q.append((child, turns + 1))
        return -1