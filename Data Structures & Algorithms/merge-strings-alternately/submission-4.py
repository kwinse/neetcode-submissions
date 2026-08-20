class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        i = 0

        while i in range(min(len(word1), len(word2))):
            res.append(word1[i])
            res.append(word2[i])
            i += 1

        res.append(word1[i:])
        res.append(word2[i:])

        return "".join(res)