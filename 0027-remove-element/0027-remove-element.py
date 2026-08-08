class Solution(object):
    def removeElement(self, nums, val):
        k=0
        for b in range(len(nums)):
            if(nums[b]!=val):
              nums[k]=nums[b]
              k+=1
        return k
           
            