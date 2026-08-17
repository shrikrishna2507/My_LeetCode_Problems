class Solution(object):
    def myAtoi(self, s):
        s = s.strip()
        if not s:
            return 0
        
        sign = 1
        start = 0
        if s[0] == '-':
            sign = -1
            start = 1
        elif s[0] == '+':
            start = 1
            
        l = []
        for c in range(start, len(s)):
            if s[c].isdigit():
                l.append(s[c])
            else:
                break
                
        if not l:
            return 0
            

        ans = 0
        for char in l:
            ans = ans * 10 + (ord(char) - ord('0'))
            
        ans *= sign
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        if ans < INT_MIN:
            return INT_MIN
        if ans > INT_MAX:
            return INT_MAX
            
        return ans