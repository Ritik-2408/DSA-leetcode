class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)

        # Prefix sums
        prefix = [0] * n
        prefix[0] = stones[0]

        for i in range(1, n):
            prefix[i] = prefix[i - 1] + stones[i]

        # Initially, the only possible final merge is all stones.
        dp = prefix[-1]

        # x must be > 1, so prefix[1] is the first usable prefix.
        for i in range(n - 2, 0, -1):
            dp = max(dp, prefix[i] - dp)

        return dp
