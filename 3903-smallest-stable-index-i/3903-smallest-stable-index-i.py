class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        
        # Precompute suffix minimums
        suffix_min = [0] * n
        curr_min = float('inf')
        for i in range(n - 1, -1, -1):
            curr_min = min(curr_min, nums[i])
            suffix_min[i] = curr_min
            
        # Iterate and keep track of prefix maximum
        curr_max = float('-inf')
        for i in range(n):
            curr_max = max(curr_max, nums[i])
            instability = curr_max - suffix_min[i]
            if instability <= k:
                return i
                
        return -1