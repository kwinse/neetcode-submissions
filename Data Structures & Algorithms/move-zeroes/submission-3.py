class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        fill = 0
        for check in range(len(nums)):
            if nums[check] != 0:
                nums[fill], nums[check] = nums[check], nums[fill]
                fill += 1