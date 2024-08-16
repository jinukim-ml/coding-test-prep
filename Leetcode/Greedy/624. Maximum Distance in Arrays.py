class Solution:
    def maxDistance(self, arrays: list[list[int]]) -> int:
        minsofar, maxsofar = arrays[0][0], arrays[0][-1]
        ans = float('-inf')
        for i in range(1, len(arrays)):
            maxdiff = max(maxsofar - arrays[i][0], arrays[i][-1] - minsofar)
            ans = max(ans, maxdiff)

            minsofar = min(minsofar, arrays[i][0])
            maxsofar = max(maxsofar, arrays[i][-1])
        return ans