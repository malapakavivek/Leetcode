class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        a=s.count(s[0])
        for i in s:
            if a!=s.count(i):
                return False
        return True