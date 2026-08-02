

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0) 
        curr = dummy
        
        j = 0  

       
        while l1 or l2 or j:

            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            s = val1 + val2 + j

            rem = s % 10

            j = s // 10

            curr.next = ListNode(rem)
            curr = curr.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next  