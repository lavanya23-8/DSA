class Solution(object):
    def subsetsWithDup(self, nums):
        nums.sort()  # sort to group duplicates together
        res = []
        
        def backtrack(start, path):
            res.append(list(path))  # record current subset
            
            for i in range(start, len(nums)):
                # skip duplicates
                if i > start and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                backtrack(i+1, path)
                path.pop()
        
        backtrack(0, [])
        return res