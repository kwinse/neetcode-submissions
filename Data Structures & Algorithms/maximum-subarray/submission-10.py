class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentSum = 0
        globalMax = nums[0]

        for n in nums:
            currentSum = max(n, currentSum + n)
            globalMax = max(globalMax, currentSum)
        return globalMax