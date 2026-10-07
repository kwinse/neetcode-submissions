class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        cur = []

        for i in range(1, numRows+1):
            if i == 1:
                cur = [1]
            else:
                last = res[len(res)-1]
                cur = [1]
                for n in range(len(last)-1):
                    cur.append(last[n] + last[n+1])
                cur.append(1)
            res.append(cur)
        return res