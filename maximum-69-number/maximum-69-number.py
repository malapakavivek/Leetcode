class Solution:
    def maximum69Number (self, num: int) -> int:
        a=str(num)
        b=a.replace("6","9",1)
        return int(b)
        