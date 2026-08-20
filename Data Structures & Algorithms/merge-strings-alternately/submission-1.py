class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        length = min(len(word1), len(word2))
        altStr = ''
        for i in range(length):
            altStr += word1[i] + word2[i]
        if len(word1) > len(word2):
            altStr += word1[length:]
        elif len(word1) < len(word2):
            altStr += word2[length:]
        return altStr
