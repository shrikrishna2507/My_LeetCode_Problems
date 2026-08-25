class Solution(object):
    def missingMultiple(self, nums, k):
      ns=set(nums)
      m=1
      while True:
        cm=m*k
        if cm not in ns:
            return cm 
        m+=1
       