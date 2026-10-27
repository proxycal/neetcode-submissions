class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        output=[1]*n
        left=1
        right=1
        product=1
        for j in range(n):
            output[j]*=left
            left*=nums[j]
        for i in range(n-1,-1,-1):
            output[i]*=right
            right*=nums[i]
        return output
  
        

            
        