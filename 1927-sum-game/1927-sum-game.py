class Solution(object):
    def sumGame(self, num):
        s = len(num)
        m = s // 2
        c1 = 0
        c2 = 0
        q1 = 0
        q2 = 0
        
        for i in range(m):
            if num[i] == '?':
                q1 += 1
            else:
                c1 += int(num[i])
                
        for i in range(m, s):
            if num[i] == '?':
                q2 += 1
            else:
                c2 += int(num[i])
                
        if (q1 + q2) % 2 != 0:
            return True
            
        return (c1 - c2) * 2 != (q2 - q1) * 9