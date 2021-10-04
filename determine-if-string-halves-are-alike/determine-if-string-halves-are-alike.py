class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        a=s[:len(s)//2]
        b=s[len(s)//2:]
        vowels=['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        c=0
        d=0
        for i in a:
            if i in vowels:
                c+=1
        for i in b:
            if i in vowels:
                d+=1
        if c==d:
            return True
        else:
            return False
        