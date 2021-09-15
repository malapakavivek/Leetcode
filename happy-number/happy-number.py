class Solution:
    def isHappy(self, n: int) -> bool:
        lis = []
        while n not in lis:
            lis.append(n)
            n = list(str(n))
            happy = 0
            for i in n:
                happy += int(i)**2
            if happy == 1:
                return True
            n = happy
        return False
              
        
      
    
                
                
                
                
            