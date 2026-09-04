class Solution:
    def firstStableIndex(self, nums: List[int], k: int) -> int:
        n = len(nums)

        for i in range(n):
            left_max = max(nums[:i+1])
            right_min = min(nums[i:])

            score = left_max - right_min

            if score <= k:
                return i

        return -1