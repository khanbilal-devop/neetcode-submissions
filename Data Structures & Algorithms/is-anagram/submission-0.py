class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        strMap = {}
        
        for i in s:
            if(i in strMap):
               strMap[i] += 1
            else:
                strMap[i] = 1
         
        for i in t:
            if(i in strMap):
                count = strMap[i]
                if count == 0:
                    return False
                else:
                   strMap[i] -= 1             
            else:
                return False
                
        return True 