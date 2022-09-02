class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        s=""
        for i in b:
            s+=str(i)
        result= pow(a,int(s),1337)
        return result