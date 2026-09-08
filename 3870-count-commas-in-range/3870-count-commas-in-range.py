class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        c=0
        if n>=1000:
            for i in range(1000,n+1):
                c+=1
            return c
        else:
            return 0

        
        