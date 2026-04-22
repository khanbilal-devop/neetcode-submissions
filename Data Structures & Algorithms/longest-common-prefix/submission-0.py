class Solution:
        def longestCommonPrefix(self, strs):
            index = 0
            matchedString = ""
        
            while(True):
                currentCharacter = ""
                for str in strs:
                    if  index > len(str) -1:
                        return matchedString
                    character = str[index]
                    if currentCharacter == "":
                        currentCharacter = character
                    elif character != currentCharacter:
                        return matchedString 
                    
                matchedString += currentCharacter        
                index +=1
        