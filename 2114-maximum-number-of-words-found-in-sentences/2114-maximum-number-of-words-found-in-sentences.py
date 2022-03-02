class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        a=[]
        for i in sentences:
            b=len(i.split())
            a.append(b)
        return max(a)
        