class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        k=1
        for b in range(1,len(nums)):
            if(nums[b]!=nums[b-1]):
                nums[k]=nums[b]
                k+=1
        return k 