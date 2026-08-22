class Solution(object):
    def checkDivisibility(self, n):
        n_str = str(n)
        
        s = 0
        p = 1
        
        for digit in n_str:
            d = int(digit)
            s += d
            p *= d
            
        if n % (s + p) == 0:
            return True
        else:
            return False