class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        leftCursor = 0
        rightCursor = len(nums) -1
        k =0
        while leftCursor <= rightCursor:
             if nums[leftCursor] == val:
                #  Check for index where can be swapped
                while nums[rightCursor] == val and rightCursor >= 0:
                    rightCursor = rightCursor -1

                # If he right index is a valid index    
                if rightCursor >= 0 and leftCursor < rightCursor:
                    nums[leftCursor] = nums[rightCursor]
                    nums[rightCursor] = val
                    k = k +1
                    rightCursor = rightCursor -1
             else:
                k = k +1  
             leftCursor = leftCursor +1       
        print(k)
        print(nums)
        return k    

        