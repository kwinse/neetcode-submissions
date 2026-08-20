class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = len(nums) - 1

        while i <= j:
            while nums[j] == val and j > i:
                j -= 1
            if nums[i] == val:
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
            else:
                i += 1
        return i