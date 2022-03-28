class Solution:
    def addDigits(self, num: int) -> int:
        b=0
        while num>=10:
            a=sorted(str(num))
            for i in range(len(a)):
                b=int(b)+int(a[i])
            num=b
            b=0
        return num