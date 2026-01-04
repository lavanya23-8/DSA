class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        low, high = 0, m
        
        while low <= high:
            i = (low + high) // 2
            j = (m + n + 1) // 2 - i
            
            left1 = float('-inf') if i == 0 else nums1[i - 1]
            right1 = float('inf') if i == m else nums1[i]
            
            left2 = float('-inf') if j == 0 else nums2[j - 1]
            right2 = float('inf') if j == n else nums2[j]
            
            # Correct partition
            if left1 <= right2 and left2 <= right1:
                if (m + n) % 2 == 0:
                    return (max(left1, left2) + min(right1, right2)) / 2.0
                else:
                    return max(left1, left2)
            
            elif left1 > right2:
                high = i - 1
            else:
                low = i + 1
