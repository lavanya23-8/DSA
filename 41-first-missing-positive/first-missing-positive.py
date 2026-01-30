class Solution(object):
    def firstMissingPositive(self, nums):
        n = len(nums)

        # Step 1: place numbers in correct index
        i = 0
        while i < n:
            correct = nums[i] - 1
            if 1 <= nums[i] <= n and nums[i] != nums[correct]:
                nums[i], nums[correct] = nums[correct], nums[i]
            else:
                i += 1

        # Step 2: find first missing
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1
