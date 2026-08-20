class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()
        oldest = nums[0]
        for i, num in enumerate(nums):
            if num in seen:
                return True
            seen.add(num)
            if len(seen) == k + 1:
                seen.remove(nums[i-k])
        return False