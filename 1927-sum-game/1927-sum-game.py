class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        diff = 0
        q = 0

        for i in range(n // 2):
            if num[i] == '?':
                q += 1
            else:
                diff += int(num[i])

        for i in range(n // 2, n):
            if num[i] == '?':
                q -= 1
            else:
                diff -= int(num[i])

        # Odd number of '?' -> Alice gets the last move
        if q % 2 != 0:
            return True

        # Bob can balance the sums only in this exact case
        return diff + (q // 2) * 9 != 0