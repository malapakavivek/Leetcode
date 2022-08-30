class Solution:
    def isPalindrome(self, x: int) -> bool:
        pal=0
        check=x
        while x>0:
            dig=x%10
            pal=pal*10+dig
            x=x//10
        if pal==check:
            return True
        else:
            return False