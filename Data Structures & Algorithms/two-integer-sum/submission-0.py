class Solution:
    def twoSum(self, nums, target): 
        seen = {}
        index = len(nums) -1;
        for num in reversed(nums):
            result = target - num
            if result in seen:
                return [index,seen[result]]
            seen[num] = index
            index -= 1;    
        