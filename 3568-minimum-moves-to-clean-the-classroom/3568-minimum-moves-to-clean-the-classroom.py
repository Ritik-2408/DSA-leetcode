from collections import deque

class Solution:
    def minMoves(self, classroom: list[str], energy: int) -> int:

        n = len(classroom)
        m = len(classroom[0])

        litter = {}
        total = 0
        sr = 0
        sc = 0

        # Find S and L
        for i in range(n):
            for j in range(m):
                if classroom[i][j] == 'S':
                    sr = i
                    sc = j

                if classroom[i][j] == 'L':
                    litter[(i, j)] = total
                    total += 1

        if total == 0:
            return 0

        target = (1 << total) - 1

        # best[r][c][mask] = maximum energy we had here
        best = [[[-1] * (1 << total) for _ in range(m)] for _ in range(n)]

        q = deque()

        q.append((sr, sc, energy, 0, 0))
        best[sr][sc][0] = energy

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:

            r, c, en, mask, moves = q.popleft()

            if mask == target:
                return moves

            for dr, dc in directions:

                nr = r + dr
                nc = c + dc

                if nr < 0 or nr >= n or nc < 0 or nc >= m:
                    continue

                if classroom[nr][nc] == 'X':
                    continue

                if en == 0:
                    continue

                new_energy = en - 1
                new_mask = mask

                # Collect litter
                if (nr, nc) in litter:
                    bit = litter[(nr, nc)]
                    new_mask = new_mask | (1 << bit)

                # Reset energy
                if classroom[nr][nc] == 'R':
                    new_energy = energy

                # Important optimization
                if new_energy <= best[nr][nc][new_mask]:
                    continue

                best[nr][nc][new_mask] = new_energy

                q.append((
                    nr,
                    nc,
                    new_energy,
                    new_mask,
                    moves + 1
                ))

        return -1