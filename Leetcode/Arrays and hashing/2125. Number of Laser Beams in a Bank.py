class Solution:
    def numberOfBeams(self, bank: list[str]) -> int:
        m = len(bank)
        res, prev = 0, 0
        for i in range(m):
            num_devices = bank[i].count('1')
            res += prev*num_devices
            if num_devices:
                prev = num_devices
        return res