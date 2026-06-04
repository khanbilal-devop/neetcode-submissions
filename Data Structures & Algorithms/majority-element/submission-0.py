class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Idneitfy Count for majority element
        majElCnt = len(nums)/2

        # Create occurence map of each element in array
        occurenceMap = {}
        for num in nums:
            if num in occurenceMap:
                occurenceMap[num] = occurenceMap[num] +1
            else:
                occurenceMap[num] = 1    

        # Iterate map and look for element exceeding the majority elemnt count
        for key in occurenceMap:
            if occurenceMap[key] > majElCnt:
                return key

        