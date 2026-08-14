class Solution(object):
    def maximumLengthSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        max_length = 0
        char_count = {}
        
        for right in range(len(s)):
            char = s[right]
           
            char_count[char] = char_count.get(char, 0) + 1
        
            while char_count[char] > 2:
                left_char = s[left]
                char_count[left_char] -= 1
                left += 1
         
            max_length = max(max_length, right - left + 1)
            
        return max_length