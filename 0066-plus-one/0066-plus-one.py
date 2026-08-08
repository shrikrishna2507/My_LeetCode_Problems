class Solution(object):
    def plusOne(self, digits):
        
        num_str = "".join(map(str, digits))
        num = int(num_str) + 1
        return [int(char) for char in str(num)]