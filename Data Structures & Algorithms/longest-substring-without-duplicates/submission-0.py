class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        seen = {}
        maxLen = 0

        for idx, r in enumerate(s):
            if r in seen and seen[r] >= l:
                l = seen[r] + 1
            seen[r] = idx
            maxLen = max(maxLen, idx-l+1)
        
        return maxLen