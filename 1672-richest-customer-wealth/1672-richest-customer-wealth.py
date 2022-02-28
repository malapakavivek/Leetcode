class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        for i in accounts: 
            a=[]
            for i in accounts:
                a.append(sum(i))
            return max(a)
        