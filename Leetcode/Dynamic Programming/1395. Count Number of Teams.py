class Solution: # DP (bottom-up)
    def numTeams(self, rating: list[int]) -> int:
        increasing = [[0] * 4 for _ in range(len(rating))]
        decreasing = [[0] * 4 for _ in range(len(rating))]

        for i in range(len(rating)):
            increasing[i][1] = 1
            decreasing[i][1] = 1
        
        for cnt in range(2,4):
            for i in range(len(rating)):
                for j in range(i+1, len(rating)):
                    if rating[i] < rating[j]:
                        increasing[j][cnt] += increasing[i][cnt-1]
                    if rating[i] > rating[j]:
                        decreasing[j][cnt] += decreasing[i][cnt-1]
        
        ans = 0
        for i in range(len(rating)):
            ans += increasing[i][3] + decreasing[i][3]
        return ans

class Solution: # DP (top-down memoization)
    def numTeams(self, rating: list[int]) -> int:
        icache = [[-1]*4 for _ in range(len(rating))]
        dcache = [[-1]*4 for _ in range(len(rating))]
        ans = 0
        for i in range(len(rating)):
            ans += self.increasing(i, 1, rating, icache) + self.decreasing(i, 1, rating, dcache)
        return ans
    
    def increasing(self, i:int, size:int, rating: list[int], cache: list[list[int]]) -> int:
        if i == len(rating):
            return 0
        
        if size == 3:
            return 1
        
        if cache[i][size] != -1:
            return cache[i][size]
        
        valid = 0
        for j in range(i+1, len(rating)):
            if rating[j] > rating[i]:
                valid += self.increasing(j, size+1, rating, cache)

        cache[i][size] = valid
        return valid
    
    def decreasing(self, i:int, size:int, rating: list[int], cache: list[list[int]]) -> int:
        if i == len(rating):
            return 0
        if size == 3:
            return 1
        if cache[i][size] != -1:
            return cache[i][size]
        
        valid = 0
        for j in range(i+1, len(rating)):
            if rating[j] < rating[i]:
                valid += self.decreasing(j, size+1, rating, cache)
        
        cache[i][size] = valid
        return valid