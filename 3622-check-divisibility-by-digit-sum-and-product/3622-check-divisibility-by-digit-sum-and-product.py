class Solution(object):
    def checkDivisibility(self, n):
        # Convert n to a string to access individual characters/digits
        n_str = str(n)
        
        
        s = sum(int(digit) for digit in n_str)
        
        p = 1
        for digit in n_str:
            p *= int(digit)
            
        if (n % (s + p) == 0):
            return True
        else:
            return False