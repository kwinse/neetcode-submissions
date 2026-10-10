class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = 0
        for nonzero in range(len(nums)):
            if nums[nonzero] != 0:
                nums[zero], nums[nonzero] = nums[nonzero], nums[zero]
                zero += 1