class Solution(object):
    def getMinDistance(self, nums, target, start):
        m = float('inf')
        for i in range(len(nums)):
            if nums[i] == target:
                m = min(m, abs(i - start))
        return m