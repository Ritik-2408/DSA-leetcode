class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        s = sum(piles)
        a=0
        for i in range(0,len(piles),2):
            a += piles[i]
        b = 0
        for j in range(len(piles)-1,-2,-2):
            b += piles[j]
        ans = max(a,b)
        res = s-ans
        if res>ans:
            return False
        return True