class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        a=0
        for i in word:
            if i==ch:
                a=word.index(ch)
            b=word[:a+1]
            c=b[::-1]
            d=word[a+1:]
            e=c+d
        return e        