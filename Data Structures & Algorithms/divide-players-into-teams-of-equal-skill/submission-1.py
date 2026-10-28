class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill = sorted(skill)
        target = skill[0] + skill[-1]
        result = 0
        i, j = 0, len(skill) -  1

        for i in range(len(skill)//2):
            a, b = skill[i], skill[-1-i]
            if a + b != target:
                return -1
            result += a * b
    
        return result