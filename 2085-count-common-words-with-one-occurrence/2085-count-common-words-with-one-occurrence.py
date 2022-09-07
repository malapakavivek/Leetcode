class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        a=Counter(words1)
        b=Counter(words2)
        c=0
        for i,j in a.items():
            if j==1 and b[i]==1:
                c+=1
        return c