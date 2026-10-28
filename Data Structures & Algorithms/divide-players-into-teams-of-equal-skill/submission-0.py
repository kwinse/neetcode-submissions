class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        target = skill[0] + skill[-1]
        result = 0
        i, j = 0, len(skill) -  1

        while i < j:
            if skill[i] + skill[j] != target:
                return -1
            result += skill[i] * skill[j]
            i+=1
            j-=1
    
        return result