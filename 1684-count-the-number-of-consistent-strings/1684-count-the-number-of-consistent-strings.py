class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        counter=len(words)
        for i in words:
            a=set(i)
            for j in a:
                if j not in allowed:
                    counter-=1
                    break
        return counter
                
        
        