class Solution:
    def minHeightShelves(self, books: list[list[int]], shelfWidth: int) -> int:
        dp = [0] * (len(books) + 1)
        dp[0], dp[1] = 0, books[0][1]
        for i in range(2, len(books)+1):
            thickness, maxheight = books[i-1]
            remaining_width = shelfWidth - thickness
            dp[i] = maxheight + dp[i-1] # create a new shelf first
            
            for j in range(i-1, -1, -1):
                if remaining_width - books[j-1][0] < 0:
                    break
                remaining_width -= books[j-1][0]
                maxheight = max(maxheight, books[j-1][1])
                dp[i] = min(dp[i], maxheight + dp[j-1])
        return dp[len(books)]