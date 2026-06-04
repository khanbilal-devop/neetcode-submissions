class Solution:
   def majorityElement(self, nums: List[int]) -> int:

        # The majority element will outnumber the other elements
        count = 0
        candidate = None
        for num in nums: 
        #    If count is zero make this as candidate 
            if count == 0:
                candidate = num
        
        # If candidate and current number same increase count
            if candidate == num:
                count = count + 1
            else:
                count = count -1
        return candidate    

        