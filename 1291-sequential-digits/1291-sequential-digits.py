class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        res = []
        sample = "123456789"
        
        # Length of sequential numbers ranges from 2 to 9
        for length in range(2, 10):
            # Generate all sequential numbers of the current length
            for start in range(10 - length):
                num = int(sample[start : start + length])
                
                # If within range, append to result
                if low <= num <= high:
                    res.append(num)
               
                elif num > high:
                    break
                    
        return res