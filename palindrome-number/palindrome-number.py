class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        a=x[::-1]
        if x==a:
            return True
        else:
            return False