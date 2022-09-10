class Solution:
    def countAsterisks(self, s: str) -> int:
        check=False
        count=0
        for ch in s:
            if ch=="|" and check:
                check = False
            elif ch=="|" and not check:
                check = True
            elif not check and ch=="*":
                count+=1
        return count
