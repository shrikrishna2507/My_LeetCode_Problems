class Solution(object):
    def largestInteger(self, nums, k):
        """:type nums: List[int] :type k: int :rtype: int"""
        n = len(nums)
       
        window_counts = {}
    
        for i in range(n - k + 1):
            sub_window = nums[i:i + k]
        
            for x in set(sub_window):
                window_counts[x] = window_counts.get(x, 0) + 1
                
        ans = -1
        for x, count in window_counts.items():
            if count == 1:
                ans = max(ans, x)
                
        return ans