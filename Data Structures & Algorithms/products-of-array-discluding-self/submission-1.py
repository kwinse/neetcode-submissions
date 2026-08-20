class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zeros = 0
         
        for num in nums:
            if num:
                prod *= num
            else:
                zeros += 1
        
        res = [0]*len(nums)
        if zeros > 1:
            return res

        for i, num in enumerate(nums):
            if zeros:
                res[i] = 0 if num else prod
            else:
                res[i] = prod // num
            
        return res