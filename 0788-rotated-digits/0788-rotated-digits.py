class Solution(object):
    def rotatedDigits(self, n):
        c = 0
        for i in range(1, n + 1):
            b = str(i)
            if '3' in b or '4' in b or '7' in b:
                continue
            if '2' in b or '5' in b or '6' in b or '9' in b:
                c += 1
        return c