class Solution(object):
    def minimumDeletions(self, nums):
        n=len(nums)
        if n==1:
            return 1
        mi=nums.index(min(nums))
        mai=nums.index(max(nums))
        i=min(mi,mai)
        j=max(mi,mai)
        o1=j+1
        o2=n-i
        o3=(i+1)+(n-j)
        return min(o1,o2,o3)
