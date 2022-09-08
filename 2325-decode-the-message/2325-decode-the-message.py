class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        ch=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        ptr=0
        d={}
        for i in key:
            if i==" " or i in d:
                continue
            else:
                d[i]=ch[ptr]
                ptr+=1
        ans=""
        for j in message:
            if j==" ":
                ans+=j
            else:
                ans+=d[j]
        return ans