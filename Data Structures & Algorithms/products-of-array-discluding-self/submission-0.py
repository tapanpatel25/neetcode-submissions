class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)

        i = 0 
        while i < len(nums):
            rsum = 1
            lsum = 1

            li = i -1
            while li >= 0 :
                lsum *= nums[li]
                li -= 1
            
            ri = i + 1
            while ri < len(nums):
                rsum *= nums[ri]
                ri += 1
            
            result[i] = lsum * rsum 

            i += 1
        
        return result
            

        

            
        