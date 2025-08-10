class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        pool = set(['1'])
        x = 1
        for i in range(1, 30):
            x *= 2
            pool.add(''.join(sorted(str(x))))
        return ''.join(sorted(str(n))) in pool