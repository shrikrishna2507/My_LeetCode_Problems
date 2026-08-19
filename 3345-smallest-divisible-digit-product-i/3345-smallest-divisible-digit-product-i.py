class Solution(object):
    def smallestNumber(self, n, t):
        """:type n: int
        :type t: int
        :rtype: int
        """
        curr = n
        while True:
            # Calculate the product of the digits of curr
            product = 1
            temp = curr
            while temp > 0:
                product *= temp % 10
                temp //= 10
            
            # Check if the digit product is divisible by t
            if product % t == 0:
                return curr
            
            curr += 1