class Solution:
    def balancedStringSplit(self, s: str) -> int:
        r_counter=0
        l_counter=0
        counter=0
        for i in s:
            if i == "R":
                r_counter+=1
            else:
                l_counter+=1
            if r_counter==l_counter:
                counter+=1
        return counter
        