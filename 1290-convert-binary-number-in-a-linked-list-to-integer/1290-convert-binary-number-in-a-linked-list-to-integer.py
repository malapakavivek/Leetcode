class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        a = ''
        node = head
        while node:
            a += str(node.val)
            node = node.next
        a = int(a,2)
        return a 
    