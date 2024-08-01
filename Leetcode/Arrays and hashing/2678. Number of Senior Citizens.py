class Solution:
    def countSeniors(self, details: list[str]) -> int:
        ans = 0
        for info in details:
            if int(info[11:13]) > 60:
                ans += 1
        return ans