class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        n = len(nums)
        
        # Initialize closest sum with first three elements
        closest_sum = nums[0] + nums[1] + nums[2]
        
        for i in range(n - 2):
            left = i + 1
            right = n - 1
            
            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                
                # Update closest_sum if current is closer to target
                if abs(curr_sum - target) < abs(closest_sum - target):
                    closest_sum = curr_sum
                
                # Move pointers
                if curr_sum < target:
                    left += 1
                elif curr_sum > target:
                    right -= 1
                else:
                    # Exact match
                    return curr_sum
        
        return closest_sum
