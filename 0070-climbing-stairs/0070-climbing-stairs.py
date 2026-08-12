class Solution(object):
    def climbStairs(self, n):
        if(n<2):
            return n
        f,s=1,2
        for i in range(3,n+1):
            t=f+s
            f=s
            s=t
        return s
        