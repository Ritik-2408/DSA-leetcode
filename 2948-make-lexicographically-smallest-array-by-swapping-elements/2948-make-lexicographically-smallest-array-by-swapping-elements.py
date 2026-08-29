class Solution:
    def lexicographicallySmallestArray(self, nums, limit):
        
        pairs = []

        for i in range(len(nums)):
            pairs.append((nums[i], i))

        pairs.sort()

        ans = nums[:]

        start = 0

        while start < len(pairs):
            end = start

            while (end + 1 < len(pairs) and
                   pairs[end + 1][0] - pairs[end][0] <= limit):
                end += 1

            values = []
            indices = []

            for i in range(start, end + 1):
                values.append(pairs[i][0])
                indices.append(pairs[i][1])

            indices.sort()

            for i in range(len(values)):
                ans[indices[i]] = values[i]

            start = end + 1

        return ans