class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        nums_set = set(nums)

        output = []
        for i in range(nums[0], nums[-1]):
            if i not in nums_set:
                output.append(i)

        return output