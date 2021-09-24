class Solution:
    def toLowerCase(self, s: str) -> str:
        a=""
        for i in s:
            if i.isupper():
                a+=i.lower()
            else:
                a+=i
        return a
        