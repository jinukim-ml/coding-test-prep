class Solution:
    def getMaximumXor(self, nums: list[int], maximumBit: int) -> list[int]:
        xor = 0
        for n in nums:
            xor ^= n
        
        res = []
        for i in range(len(nums)-1, -1, -1):
            binary = bin(xor)[2:]
            ans = '' 
            for bit in binary:
                if bit == '1':
                    ans += '0'
                else:
                    ans += '1'
            ans = '1' * (maximumBit - len(binary)) + ans
            res.append(int(ans, 2))
            xor ^= nums[i]
        return res