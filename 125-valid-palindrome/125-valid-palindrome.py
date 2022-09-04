class Solution:
    def isPalindrome(self, s: str) -> bool:
        a=""
        b=s.lower()
        for i in b:
            if i.isalpha() or i.isdigit():
                a+=i
        if a==a[::-1]:
            return True