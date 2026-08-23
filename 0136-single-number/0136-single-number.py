class Solution(object):
    def singleNumber(self, nums):
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
            
        for num in counts:
            if counts[num] == 1:
                return num