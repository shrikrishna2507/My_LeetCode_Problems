class Solution(object):
    def isHappy(self, n):
        seen=set()
        while n!=1 and n not in seen:
            seen.add(n)
            ts=0
            n=sum(int(d)**2 for d in str(n))
        return n==1