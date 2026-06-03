class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            # Sorting each string
            key = "".join(sorted(s)) 
            # For String with matching characters the key would be same  
            if key not in groups:
                groups[key] = []
            # Appending string with same key (anagrams) into same list    
            groups[key].append(s)
            #In the end printing all the values of the map as list
        return list(groups.values())
        