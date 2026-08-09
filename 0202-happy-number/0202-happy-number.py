class Solution(object):
    def isHappy(self, n):
        seen=set()
        while n!=1 and n not in seen:
            seen.add(n)
            ts=0
            for d in str(n):
                ts+=int(d)**2
            n=ts
        return n==1