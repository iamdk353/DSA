class Solution:
    def isPalindrome(self, s: str) -> bool: 
        l=0
        r=len(s)-1

        while(l<r):
            if self.isNonAlphaNumeric(s[l]):
                l+=1
                continue
            if self.isNonAlphaNumeric(s[r]):
                r-=1
                continue
           
            if (s[l].lower() != s[r].lower()):
                return False
            l+=1
            r-=1
            
        return True
    def isNonAlphaNumeric(self,s:str)->bool:
            return (not((ord(s)>=ord("a") and ord(s)<=ord("z")) 
                    or( ord(s)>=ord("A") and ord(s)<=ord("Z")) 
                    or ( ord(s)>=ord("0") and ord(s)<=ord("9"))))

                
            
            
            
        
        


