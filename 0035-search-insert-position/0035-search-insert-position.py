class Solution(object):
    def searchInsert(self, nums, target):
       h=len(nums)-1
       l=0
       while(l<=h):
        mid=(h+l)/2
        if(nums[mid]==target):
            return mid
        elif nums[mid]<target:
            l=mid+1
        elif nums[mid]>target:
            h=mid-1
       return l